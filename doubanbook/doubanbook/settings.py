# Scrapy settings for doubanbook project
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

BOT_NAME = 'doubanbook'

SPIDER_MODULES = ['doubanbook.spiders']
NEWSPIDER_MODULE = 'doubanbook.spiders'


DOWNLOAD_DELAY = 3
COOKIES_ENABLED = False

DOWNLOADER_MIDDLEWARES = {
    #'doubanbook.middleware.CustomHttpProxyMiddleware': 543,
    'doubanbook.middleware.CustomUserAgentMiddleware': 545,
}

########### Item pipeline
ITEM_PIPELINES = {
    #'doubanbook.pipelines.JsonWithEncodingPipeline': 300,
    #'doubanbook.pipelines.RedisPipeline': 301,
    'doubanbook.pipelines.MongoDBPipeline': 302,
}

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'scrapy'
MONGODB_COLLECTION = 'douban_book'
MONGODB_UNIQ_KEY = 'link'
###########

# Set your own download folder
DOWNLOAD_FILE_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "download_file")

LOG_LEVEL = 'INFO'

