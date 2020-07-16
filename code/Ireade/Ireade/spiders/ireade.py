# -*- coding: utf-8 -*-
import scrapy
# import time


class IreadeSpider(scrapy.Spider):
    name = 'ireade'  # 爬虫名
    allowed_domains = ['ireade.com']  # 爬取的范围
    start_urls = ['http://www.ireader.com/index.php?ca=booksort.index&pca=channel.index']  # 起始站点

    def parse(self, response):
        # div_difgenre_list = response.xpath("//div[@class='content']/div[@class='genre']/div[@class='difgenre']")
        # channel_list_url = div_difgenre_list[0].xpath("./div//li/a/@href").extract()
        # for channel_url in channel_list_url:
        #     yield scrapy.Request(channel_url, callback=self.parse)
        li_list = response.xpath("//div[@class='show']/ul[@class='newShow']/li")
        for li in li_list:
            item = {"book_name": li.xpath("./div[@class='bookMation']/h3/a/text()").extract_first(),
                    "author": li.xpath("./div[@class='bookMation']/p[@class['tryread']]/text()").extract_first().replace("\t", ""),
                    "viewing_times": li.xpath("./div[@class='bookMation']/span/text()").extract()[-1].replace(" ", "").replace("\n", ""),
                    "synopsis": li.xpath("./div[@class='bookMation']/p[@class='introduce']/text()").extract_first().replace("\n", ""),
                    "img_url": li.xpath(".//img/@src").extract_first()}
            url = li.xpath("./div[@class='bookMation']/h3/a/@href").extract_first()
            yield scrapy.Request(url, callback=self.parse1, dont_filter=True, meta={'item': item})
            # yield item
            # print(item)
        next_page_url = response.xpath("//div[@class='changepage']/span/a")[-1].xpath("./@href").extract_first()
        print(next_page_url)
        # time.sleep(3)
        # if next_page_url is not None:
        #     yield scrapy.Request(next_page_url, callback=self.parse, dont_filter=True, )

    def parse1(self, response):
        item = response.meta["item"]
        item["Price"] = response.xpath("//div[@class='bookR']/div[@class='bookinf02']/div[@class='left']//i/text()").extract_first()[3:]
        print(item)
