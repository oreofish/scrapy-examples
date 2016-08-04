import re
import json
from urlparse import urlparse
import urllib
import pdb


from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from scrapy.loader import ItemLoader

from misc.log import *
from misc.spider import CommonSpider


class doubanmovieSpider(CommonSpider):
    name = "doubanmovie"
    allowed_domains = ["movie.douban.com"]

    start_urls = []
    #for year in range(1895, 2016):
    for year in range(1987, 1988):
        start_urls.append("https://movie.douban.com/tag/" + str(year))

    rules = [
        Rule(sle(allow=("/tag/[0-9]{4}.start=[0-9]{2,4}"), restrict_xpaths="//div[@class='article']"), follow=True),
        Rule(sle(allow=("/subject/[0-9]+/$"), restrict_xpaths="//div[@class='article']"), callback='parse_subject', follow=True),
    ]

    def parse_subject(self, response):
        info('Parse '+response.url)
        l = ItemLoader({}, response.selector)
        l.add_value('link', response.url)
        l.add_css('title', '#content h1 span[property]::text')
        l.add_css('year', '#content h1 span[class]::text')
        l.add_css('star', '.rating_num::text')
        return l.load_item()


    def closed(self, reason):
        info("DoubanBookSpider Closed:" + reason)

