# -*- coding: utf-8 -*-
import scrapy


class A51jobSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['51job.comm']
    start_urls = ['https://search.51job.com/list/020000,000000,0000,32,9,99,+,2,1.html']

    def parse(self, response):
        div_list = response.xpath("//div[@id='resultList']//div[@class='el']")

        for div in div_list:
            item = {"professional": div.xpath("./p//a/@title").extract_first(),
                    "The_company": div.xpath("./span[@class='t2']/a/@title").extract_first(),
                    "place": div.xpath("./span[@class='t3']/text()").extract_first(),
                    "salary": div.xpath("./span[@class='t4']/text()").extract_first(),
                    "date": div.xpath("./span[@class='t5']/text()").extract_first()}
            yield item
        # 找到下一页url地址
        next_url = response.xpath("//li[@class='bk']/a[contains(text(), '下一页')]/@href").extract_first()
        print(next_url)
        if next_url is not None:
            # print("_" * 20)
            yield scrapy.Request(next_url, callback=self.parse, dont_filter=True)
    #
    # def parse1(self, response):
    #
    #     a = response.xpath("//div[@id='wrapper']")
    #     print(a)


