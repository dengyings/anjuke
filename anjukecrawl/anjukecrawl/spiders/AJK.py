# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from ..items import AnjukecrawlItem
import os

os.environ["http_proxy"] = "https://139.196.125.96:8088"
class AjkSpider(CrawlSpider):
    name = 'AJK'
    allowed_domains = ['guangzhou.anjuke.com']
    start_urls = ['https://guangzhou.anjuke.com/sale/']

    rules = (
        Rule(LinkExtractor(allow=r'p2/#filtersort'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print("1"*100)
        nexturls = re.findall(r'<a data-from[\s\S]*?href="([\s\S]*?)"',response.text)
        for nexurl in nexturls:
            request = scrapy.Request(url=nexurl, callback=self.house_infos)
            yield request

    def house_infos(self, response):
        title = re.findall(r'<h3 class="long-title">([\s\S]*?)</h3>',response.text)
        housenumber = response.xpath('//span[@id="houseCode"]/text()').extract()
        time = re.findall(r'id="houseCode"[\s\S]*?</span>([\s\S]*?)</span>', response.text)
        Agent = response.xpath('//div[@class="brokercard-name"]/text()').extract()
        grade = re.findall(r'class="score-num">([\s\S]*?)</em>', response.text)[0]
        Item = AnjukecrawlItem(title=title,housenumber=housenumber,time=time,Agent=Agent,grade=grade)
        yield Item
