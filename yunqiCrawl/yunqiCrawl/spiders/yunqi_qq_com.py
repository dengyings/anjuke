# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re
from ..items import YunqicrawlItem

class YunqiQqComSpider(CrawlSpider):
    name = 'yunqi.qq.com'
    allowed_domains = ['yunqi.qq.com']
    start_urls = ['http://yunqi.qq.com/bk/so2/n30p1']

    rules = (
        Rule(LinkExtractor(allow=r'/bk/so2/n30p\d+'), callback='parse_book_item', follow=True),
    )

    def parse_book_item(self, response):
        #pattent1 = re.compile(r'<div class="book">[\s\S]*></dd>')
        #books = re.findall(pattent1, response.url)
        books = response.xpath('.//div[@class="book"]')
        for book in books:
            #pattent1 = re.compile(r'<div class="book">[\s\S]*></dd>')
            #BookName = book.Xpath("")
            #BookId = book.Xpath("")
            BookName = re.findall(r'<a id="book[\s\S]*?html">([\s\S]*?)</a>', book.extract())
            BookId = re.findall(r'<a id="book_(\d+)"', book.extract()) 
            #BookId = re.findall(r'<a id="book_(\d+)"', book) 
            bookListItem = YunqicrawlItem(BookName=BookName,BookId=BookId) 
            yield bookListItem





