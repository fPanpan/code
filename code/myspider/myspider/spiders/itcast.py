# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'     # 爬虫名
    allowed_domains = ['itcast.cn'] # 爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']  # 爬取初始url地址

    def parse(self, response):
        li_list = response.xpath("//div[@class='tea_con']//li")
        for li in li_list:
            item = {"name": li.xpath(".//h3//text()").extract_first(),
                    "title": li.xpath(".//h4/text()").extract_first()}
            yield item
            # print(item)

