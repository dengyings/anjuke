# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from items import ZolimageItem, ZolimageurlItem


class ZolimagePipeline(object):
    
    def process_item(self, item, spider):
        if isinstance(item,ZolimageItem):
            with open("zolname.json", "ab") as f:
                text1 = json.dumps(dict(item),ensure_ascii=False)+'\n'
                f.write(text1.encode('utf-8'))
        else:
            with open("zolnameurl.json", "ab") as f:
                text2 = json.dumps(dict(item),ensure_ascii=False)+'\n'
                f.write(text2.encode('utf-8'))
        return item


