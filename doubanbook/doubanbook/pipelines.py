# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis
from scrapy.conf import settings
from misc.log import *
from scrapy import signals


import json
import codecs
from collections import OrderedDict


class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('data_utf8.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()


class RedisPipeline(object):

    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379)

    def process_item(self, item, spider):
        if not item['id']:
            print 'no id item!!'

        str_recorded_item = self.r.get(item['id'])
        final_item = None
        if str_recorded_item is None:
            final_item = item
        else:
            ritem = eval(self.r.get(item['id']))
            final_item = dict(item.items() + ritem.items())
        self.r.set(item['id'], final_item)

    def spider_closed(self, spider):
        return


class MongoDBPipeline(object):
    def __init__(self):
        import pymongo
        connection = pymongo.MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        self.db = connection[settings['MONGODB_DB']]
        self.collection = self.db[settings['MONGODB_COLLECTION']]
        if self.__get_uniq_key() is not None:
            self.collection.create_index(self.__get_uniq_key(), unique=True)

    def process_item(self, item, spider):
        if self.__get_uniq_key() is None:
            self.collection.insert(dict(item))
        else:
            self.collection.update(
                            {self.__get_uniq_key(): item[self.__get_uniq_key()]},
                            dict(item),
                            upsert=True)
        debug("Item wrote to MongoDB database %s/%s" %
                    (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']))
        return item

    def __get_uniq_key(self):
        if not settings['MONGODB_UNIQ_KEY'] or settings['MONGODB_UNIQ_KEY'] == "":
            return None
        return settings['MONGODB_UNIQ_KEY']