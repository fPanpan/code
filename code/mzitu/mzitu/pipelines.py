# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from hashlib import md5


class MzituPipeline(object):
    def process_item(self, item, spider):
        os.chdir(r"D:\images")
        if not os.path.exists(item["title"]):
            try:
                os.mkdir(item["title"])
            except NotADirectoryError as e:
                print(e)
                return None
        filename = "{0}/{1}.{2}".format(item["title"], md5(item["img"]).hexdigest(), "jpg")
        with open(filename, "wb") as f:
            f.write(item["img"])

        return item
