import re
import json


from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from misc.spider import CommonSpider

from doubanbook.items import *
from misc.log import *


class DoubanBookSpider(CommonSpider):
    name = "doubanbook"
    allowed_domains = ["douban.com"]
    start_urls = [
        "https://book.douban.com/tag/"
    ]
    rules = [
        #Rule(sle(allow=("/subject/\d+/$")), callback='parse_page'),
        Rule(sle(allow=("/tag/[^/]+$", )), follow=True, callback='parse_tag'),
        #Rule(sle(allow=("/tag/$", )), follow=True),
    ]

    subject_css_rules = {
        '.subject-item': {
            'title': 'h2 a::text',
            'link':  'h2 a::attr(href)',
            'pub':   '.pub::text',
            'star':  '.star .rating_nums::text',
            'times': '.star .pl::text',
            'desc':  'p::text',
            'price': '.ft .buy-info a::text',
        }
    }

    def parse_tag(self, response):
        info('======================= Parse '+response.url)
        x = self.parse_with_rules(response, self.subject_css_rules, dict)
        return x[0].values()[0]

    def process_request(self, request):
        info('process ' + str(request))
        return request

    def closed(self, reason):
        info("DoubanBookSpider Closed:" + reason)
