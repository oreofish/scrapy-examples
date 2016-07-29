# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class githubRepoItem(Item):
    # define the fields for your item here like:
    link = Field()
    desc = Field()
    lang = Field()
    star = Field()
    fork = Field()

