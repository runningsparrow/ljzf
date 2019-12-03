# -*- coding: utf-8 -*-
import scrapy


class SpiderljzfSpider(scrapy.Spider):
    name = 'spiderljzf'
    allowed_domains = ['https://sh.lianjia.com/zufang/']
    start_urls = ['http://https://sh.lianjia.com/zufang//']

    def parse(self, response):
        pass
