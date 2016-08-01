import re
import json


from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider

from scrapy.spiders import CrawlSpider, Rule


from z_jd_com.items import *
import time
from misc.log import *


class DoubanBookSpider(Spider):
    name = "z_jd_com"
    allowed_domains = ["z.jd.com"]
    start_urls = [
        "http://z.jd.com/project/details/64570.html",
    ]

    def parse(self, response):
        items = []
        sel = Selector(response)
        counts = sel.css('.t-people span::text').extract()
        ISOTIMEFORMAT = '%Y-%m-%d%X'
        timestamp = time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
        for c in counts:
            items.append(c.strip())
        result = ZJdComItem()
        result['time'] = timestamp
        result['count'] = items
        info('==== parsed ' + str(result))
        return result

    def process_request(self, request):
        info('==== process ' + str(request))
        return request

    def closed(self, reason):
        info("==== ZJdComSpider Closed:" + reason)
