# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from ..items import CnblogspiderItem

class CnblogsSpider(CrawlSpider):
    name = 'cnblogs'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://cnblogs.com/qiyeboy/default.html?page=1']

    rules = (
        Rule(LinkExtractor(allow=r'/qiyeboy/default.html\?page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        parses = response.xpath(".//*[@class='day']")
        for paper in parses:
            url = paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
            title = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
            content = paper.xpath(".//*[@class='postCon']/a/text()").extract()
            item = CnblogspiderItem(url=url,title=title,time=time,content=content)
            request = scrapy.Request(url=url, callback=self.parse_body)
            request.meta['item'] = item
            yield request

    def parse_body(self,response):
        item = response.meta['item']
        body = response.xpath(".//*[@class='postBody']")
        #cimage_urls = re.findall(r'<img style[\s\S]*?src="([\s\S]*?)" alt', body.extract())[0]
        #item['cimage_urls'] = cimage_urls
        item['cimage_urls'] = body.xpath('.//img/@src').extract()
        yield item
 #   next_page = Selector(response).re(r'<a href="(\S*)">下一页</a>')
 #   if next_page:
 #       yield scrapy.Request(ure=next_page[0],callback=self.parse_item)