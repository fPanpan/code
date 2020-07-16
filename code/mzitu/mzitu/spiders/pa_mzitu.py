# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class PaMzituSpider(CrawlSpider):
    name = 'pa_mzitu'
    allowed_domains = ['girlsky.cn', 't2.ituba.cc']
    start_urls = ['http://www.girlsky.cn/mntp/']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.girlsky.cn/mntp/[a-z]+?/$'), follow=True),
        Rule(LinkExtractor(allow=r'http://www.girlsky.cn/mntp/rtys/\d+?.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/mntp/list_\d+?_\d+?.html'), follow=True),
        Rule(LinkExtractor(allow=r'//www.girlsky.cn/mntp/[a-z]+?/\d+?_\d+?.html'),callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # print(response.url)
        # print('*' * 50)
        item = {}
        img_url = response.xpath('//div[@id="ArticleId8"]/div[1]/a/img/@src').extract_first()
        item["img_url"] = "http:" + img_url if img_url[:5] != "http:" else img_url
        item['title'] = response.xpath("//div[@class='ArticleTitle']/h1/text()").extract_first().split("(")[0]
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        print(item)
        yield scrapy.Request(
            item["img_url"], callback=self.parse1, meta={"item": item}
        )
        # return item

    def parse1(self, response):
        item = response.meta["item"]
        item["img"] = response.body
        print("*" * 50)
        print(item)
        yield item
