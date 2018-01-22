# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem

class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    #allowed_domains = ['douyucdn.cn']
    #start_urls = ['http://douyucdn.cn/']
	#爬取动态网站是利用json，下面为json地址
    baseUrl="http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    offset=0
    start_urls=[baseUrl+str(offset)]

    def parse(self, response):
		#格式转换，先将response的内容转为可处理的json格式
        data_list=json.loads(response.body)['data']
        #print(content['data'])
        if len(data_list) == 0:
            return ;
        for data in data_list:
            item=DouyuItem()
            item['nickname']=data['nickname']
            item['imagelink']=data['vertical_src']
            
            yield item
            
            
        #self.offset += 20
        #yield scrapy.Request(self.baseUrl+str(self.offset),callback=self.parse)
        
        
