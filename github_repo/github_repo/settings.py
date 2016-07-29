# Scrapy settings for github_repo project
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

BOT_NAME = 'github_repo'

SPIDER_MODULES = ['github_repo.spiders']
NEWSPIDER_MODULE = 'github_repo.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'github_repo (+http://www.yourdomain.com)'

DOWNLOADER_MIDDLEWARES = {
   # 'misc.middleware.CustomHttpProxyMiddleware': 400,
    'misc.middleware.CustomUserAgentMiddleware': 401,
}

########### Item pipeline
ITEM_PIPELINES = {
    #'misc.pipelines.JsonWithEncodingPipeline': 300,
    'misc.pipelines.MongoDBPipeline': 302,
}

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'scrapy'
MONGODB_COLLECTION = 'github_repo'
MONGODB_UNIQ_KEY = 'link'
###########

LOG_LEVEL = 'INFO'

DOWNLOAD_DELAY = 1
