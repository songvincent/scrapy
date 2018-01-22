# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
	#允许的范围
    allowed_domains = ['']
    start_urls = ['http:///']

    def parse(self, response):
	    print(response.body)
	    pass