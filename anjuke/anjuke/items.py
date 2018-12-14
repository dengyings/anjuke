# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnjukeItem(scrapy.Item):
    Community_name = scrapy.Field()
    Price = scrapy.Field()
    Property_type = scrapy.Field()   #物业类型
    Developers = scrapy.Field()
    Regional_location = scrapy.Field()
    address = scrapy.Field()
    Apartment = scrapy.Field() #户型
    Latest_opening = scrapy.Field()
    Hand_time = scrapy.Field() #交楼时间
    Plot_ratio = scrapy.Field() #容积率
    Afforestation_rate = scrapy.Field() #绿化
    Planning_households = scrapy.Field() #规划户数
    Property_management_fee = scrapy.Field()
    Property_company = scrapy.Field()
    Number_of_cars = scrapy.Field()



