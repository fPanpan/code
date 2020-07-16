# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class IreadePipeline(object):
    def process_item(self, item, spider):
        with open("./出版_小说.json", 'a', encoding="utf-8") as f:
            json.dump(item, f, ensure_ascii=False)
            f.write("\n")
        return item
