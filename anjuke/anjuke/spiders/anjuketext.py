# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import AnjukeItem
import re

class AnjuketextSpider(CrawlSpider):
    name = 'anjuketext'
    allowed_domains = ['https://fs.fang.anjuke.com']
    start_urls = ['https://fs.fang.anjuke.com/loupan/canshu-447165.html?from=loupan_tab']

    rules = (
        Rule(LinkExtractor(allow=r'https://fs.fang.anjuke.com/loupan/canshu-447165.html/?from=loupan_tab'), 
        callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        info = response.xpath('//div[@id="container"]')[0]

        houseinfos = response.xpath('//ul[@class="list"]')[0:4]
        houseinfo = houseinfos.xpath('//li')
        d = {}
        for i in houseinfo:
            keys = i.xpath('//div')[0]
            key1 =  keys.xpath('string(.)').extract()[0]
            key = key1.replace(" ","")
            values = i.xpath('//div')[1]
            value = values.xpath('string(.)').extract()[0]
            d[key] = value.replace(" ","")
            print(d,"u"*100)
                #print(info,"a"*100)
        Community_name = info.xpath('//div[@class="des"]/a/text()').extract()[0]
        #Community_name = re.findall(r'楼盘名称[\s\S]*?href="[\s\S]*?">([\s\S]*?)<', info.extract())
        print(Community_name,"C"*100)
        #Price = re.findall(r'参考单价[\s\S]*?span[\s\S]*?">([\s\S]*?)<', info.extract())
        Prices = info.xpath('//div[@class="des"]')[2]
        Price = Prices.xpath('/text()')
        print(Price,"A"*100)
        try:
            Property_type = d['物业类型']
        except:
            Property_type = "abc"
        #Property_type = re.findall(r'物业类型[\s\S]*?des">([\s\S]*?)<', info.extract())                           
        try:
            Developers = d['开发商'] or 0
        except:
            Developers = "abc"
        #Developers = re.findall(r'开发商[\s\S]*?href="[\s\S]*?">([\s\S]*?)<', info.extract())                              
        #Regional_location1 = re.findall(r'区域位置[\s\S]*?href="[\s\S]*?">([\s\S]*?)<', info.extract())
        #Regional_location2 = re.findall(r'区域位置[\s\S]*?href="[\s\S]*?href="[\s\S]*?">([\s\S]*?)<', info.extract())
        #Regional_location = str(Regional_location1) + str(Regional_location2)
        Regional_location = "abc"
        #address = re.findall(r'楼盘地址[\s\S]*?des">([\s\S]*?)<', info.extract())   
        address = "abc"
        #Apartment1 = re.findall(r'楼盘户型([\s\S]*?)最新开盘', info.extract())[0]
        #Apartment = re.findall(r'huxing">([\s\S]*?户型[\s\S]*?)<', Apartment1)
        Apartment = "abc"                           
        Latest_opening = re.findall(r'基本信息([\s\S]*?)楼盘名称', info.extract())  
        print(Latest_opening,"DD"*100)                            
        Hand_time = re.findall(r'交房时间[\s\S]*?des">([\s\S]*?)<', info.extract())                              
        Plot_ratio = re.findall(r'容积率[\s\S]*?des">([\s\S]*?)<', info.extract())                              
        Afforestation_rate = re.findall(r'绿化率[\s\S]*?des">([\s\S]*?)<', info.extract())                              
        Planning_households = re.findall(r'规划户数[\s\S]*?des">([\s\S]*?)<', info.extract())                              
        Property_management_fee = re.findall(r'物业管理费[\s\S]*?des">([\s\S]*?)<', info.extract())                              
        Property_company = re.findall(r'物业公司[\s\S]*?des">([\s\S]*?)<', info.extract())                              
        Number_of_cars = re.findall(r'车位数[\s\S]*?des">([\s\S]*?)<', info.extract())                              
        Item = AnjukeItem(Community_name=Community_name,Price=Price,Property_type=Property_type,Developers=Developers,
        Regional_location=Regional_location,address=address,Apartment=Apartment,Latest_opening=Latest_opening,
        Hand_time=Hand_time,Plot_ratio=Plot_ratio,Afforestation_rate=Afforestation_rate,Planning_households=Planning_households,
        Property_management_fee=Property_management_fee,Property_company=Property_company,Number_of_cars=Number_of_cars)
        yield Item
              