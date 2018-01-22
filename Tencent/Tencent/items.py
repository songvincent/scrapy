# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    #职位名称
    positionName = scrapy.Field()
    #职位类别
    positionType=scrapy.Field()
    #人数
    peopleNumber=scrapy.Field()
    #地点
    workLocation=scrapy.Field()
    #发布时间
    distributeTime=scrapy.Field()