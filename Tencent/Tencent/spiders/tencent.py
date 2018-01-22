# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    baseUrl='http://hr.tencent.com/position.php?&start='
    
    offset=0
    start_urls = [baseUrl+str(offset)]

    def parse(self, response):
        
        node_list=response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        
        for node in node_list:
            item=TencentItem()
            if len(node.xpath("./td[1]/a/text()").extract()) >0:
                item['positionName']=node.xpath("./td[1]/a/text()").extract()[0]
            else:
                #item['positonName']=""
                continue
                
            if len(node.xpath("./td[2]/text()").extract()) >0:
                item['positionType']=node.xpath("./td[2]/text()").extract()[0]
            else:
                item['positionType']=""
            
            if len(node.xpath("./td[3]/text()").extract()) >0:
                item['peopleNumber']=node.xpath("./td[3]/text()").extract()[0]
            else:
                item['peopleNumber']=""
                
            if len(node.xpath("./td[4]/text()").extract()) > 0:
                item['workLocation']=node.xpath("./td[4]/text()").extract()[0]
            else:
                item['workLocation']=""
                
            if len(node.xpath("./td[5]/text()").extract()) > 0:
                item['distributeTime']=node.xpath("./td[5]/text()").extract()[0]
            else:
                item['distributeTime']=""
                
            yield item
            
        #offset += 10
        # if self.offset< 20:
            # self.offset += 10
            # newUrl=self.baseUrl+str(self.offset)
            # yield scrapy.Request(newUrl,callback=self.parse)
            
        if len (node.xpath("//a[@class='noactive' and @id='next']")) ==0:
            url=node.xpath("//a[@id='next']/@href").extract()
            yield scrapy.Request('http://hr.tencent.com/'+url[0],callback=self.parse)
        