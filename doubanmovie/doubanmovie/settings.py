# Scrapy settings for doubanmovie project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import sys
import os
from os.path import dirname
path = dirname(dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(path)
from misc.log import *

BOT_NAME = 'doubanmovie'
NEWSPIDER_MODULE = BOT_NAME + '.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]


DOWNLOADER_MIDDLEWARES = {
    'misc.middleware.CustomFreeProxyMiddleware': 400,
    'misc.middleware.CustomUserAgentMiddleware': 401,
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 500,
}
HTTPCACHE_ENABLED = True
HTTPCACHE_DIR = BOT_NAME+'cache'
HTTPCACHE_POLICY = 'scrapy.extensions.httpcache.DummyPolicy'
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# Set your own download folder
DOWNLOAD_FILE_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "download_file")


########### Item pipeline
ITEM_PIPELINES = {
    #'misc.pipelines.JsonWithEncodingPipeline': 300,
    'misc.pipelines.MongoDBPipeline': 302,
}
MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27016
MONGODB_DB = 'scrapy'
MONGODB_COLLECTION = BOT_NAME
MONGODB_UNIQ_KEY = 'link'
###########


LOG_LEVEL = 'INFO'
DOWNLOAD_DELAY = 1
COOKIES_ENABLED = False

