# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from ..items import ZolimageItem, ZolimageurlItem


class ZolSpider(CrawlSpider):
    name = 'ZOL'
    allowed_domains = ['desk.zol.com.cn']
    start_urls = ['http://desk.zol.com.cn/dongman/haizeiwang/']

    rules = (
        Rule(LinkExtractor(allow=r'/dongman/haizeiwang/.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        lis = response.xpath('.//li[@class="photo-list-padding"]')
        for li in lis:
            urls = re.findall(r'href="([\s\S]*?)"', li.extract())[0] 
            newurl = "http://desk.zol.com.cn" + str(urls)        
            request = scrapy.Request(url=newurl, callback=self.parse_body)
            yield request

    def parse_body(self,response):
        pattens = response.xpath('.//*[@id="showImg"]/li')
        for patten in pattens:
            urls = re.findall(r'href="([\s\S]*?)"', patten.extract())[0] 
            newurl1 = "http://desk.zol.com.cn" + str(urls)
            request = scrapy.Request(url=newurl1, callback=self.parse_body_image)
            yield request

    def parse_body_image(self,response):
        pattens = response.xpath('.//dd[@id="tagfbl"]/a')
        for patten in pattens:
            urls = response.xpath('.//a[@id="1920x1200"]/@href').extract_first()
            newurl2 = "http://desk.zol.com.cn" + str(urls)
            print(newurl2,"6"*100)
            request = scrapy.Request(url=newurl2, callback=self.parse_body_url)
            yield request

    def parse_body_url(self,response):
        imageurl = response.xpath('.//img/@src').extract()
        urlitem = ZolimageurlItem(imageurl=imageurl)
        yield urlitem