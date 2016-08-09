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

BOT_NAME = 'doubanmovie'
NEWSPIDER_MODULE = BOT_NAME + '.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
LOG_LEVEL = 'INFO'
DOWNLOAD_DELAY = 1
COOKIES_ENABLED = False

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27016
MONGODB_DB = 'scrapy'
MONGODB_COLLECTION = BOT_NAME
MONGODB_UNIQ_KEY = 'link'

BASE_DIR = '/Users/xing/Documents/git/python/scrapy-examples/scrapyd/'
RETRY_TIMES = 10  # Retry many times since proxies often fail
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]  # Retry on most error codes since proxies fail for many reasons
PROXY_LIST = BASE_DIR + 'proxylist.txt'
BAD_PROXY_LIST = BASE_DIR + 'bad_proxylist.txt'
HTTPCACHE_ENABLED = True
HTTPCACHE_DIR = BASE_DIR + BOT_NAME + '.cache'
HTTPCACHE_POLICY = 'scrapy.extensions.httpcache.DummyPolicy'
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
DOWNLOAD_FILE_FOLDER = BASE_DIR + "download_file"  # Set your own download folder
AUTO_NO_PROXY_TIMEOUT = 200
AUTO_PROXY_FILE = BASE_DIR + 'autoproxylist.txt'

# ========================= DOWNLOADER_MIDDLEWARES =========================
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    'common.auto_proxy.HttpProxyMiddleware.HttpProxyMiddleware': 100,
    # 'common.randomproxy.RandomProxy': 100,
    # 'common.middleware.CustomFreeProxyMiddleware': 101,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    'common.middleware.CustomUserAgentMiddleware': 401,
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 500,
}


# ========================= ITEM_PIPELINES =========================
ITEM_PIPELINES = {
    # 'doubanmovie.common.pipelines.JsonWithEncodingPipeline': 300,
    'common.pipelines.MongoDBPipeline': 302,
}
