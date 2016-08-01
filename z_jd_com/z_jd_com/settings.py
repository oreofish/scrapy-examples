# Scrapy settings for z.jd.com project
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

BOT_NAME = 'z_jd_com'

SPIDER_MODULES = ['z_jd_com.spiders']
NEWSPIDER_MODULE = 'z_jd_com.spiders'


DOWNLOAD_DELAY = 3
COOKIES_ENABLED = False

DOWNLOADER_MIDDLEWARES = {
    #'z.jd.com.middleware.CustomHttpProxyMiddleware': 543,
    #'z_jd_com.middleware.CustomUserAgentMiddleware': 545,
}

########### Item pipeline
ITEM_PIPELINES = {
    #'z.jd.com.pipelines.JsonWithEncodingPipeline': 300,
    #'z.jd.com.pipelines.RedisPipeline': 301,
    'z_jd_com.pipelines.MongoDBPipeline': 302,
}

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'scrapy'
MONGODB_COLLECTION = 'z.jd.com'
MONGODB_UNIQ_KEY = 'time'
###########

# Set your own download folder
DOWNLOAD_FILE_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "download_file")

LOG_LEVEL = 'INFO'

