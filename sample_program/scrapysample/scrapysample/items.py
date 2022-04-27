# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapysampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 画像
    src = scrapy.Field()
    # 書名
    name = scrapy.Field()
    # 価格
    price = scrapy.Field()
