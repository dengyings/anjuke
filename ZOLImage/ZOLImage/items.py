# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZolimageItem(scrapy.Item):
    image = scrapy.Field()
    time = scrapy.Field()

class ZolimageurlItem(scrapy.Item):
    imageurl = scrapy.Field()
    images = scrapy.Field()