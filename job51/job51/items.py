# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Job51Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #公司名字
    company_name=scrapy.Field()
    #公司url
    company_url=scrapy.Field()
    #公司详细信息
    company_info=scrapy.Field()
    #公司地址
    company_address=scrapy.Field()
    #pass
