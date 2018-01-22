# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import scrapy
from Douyu.settings import IMAGES_STORE as ims
from scrapy.pipelines.images import ImagesPipeline

#ImagesPipeline 位于 C:\Users\as\Miniconda3\Lib\site-packages\scrapy\pipelines\images.py
#其中ImagesPipeline可以处理图片，进行图片处理
class DouyuPipeline(ImagesPipeline):
    # def process_item(self, item, spider):
        # return item
    def get_media_requests(self,item,info):
        image_link=item['imagelink']
        yield scrapy.Request(image_link)
 #item_completed 中的results可以获得文件路径，然后利用os.rename改变文件路径与文件名
    def item_completed(self,results,item,info):
        image_path=[x["path"] for ok,x in results if ok]
        # print(image_path[0])
        # print()
        os.rename(ims+'/'+image_path[0],ims+'/'+item['nickname']+'.jpg')
		#下面这个很重要，当心忘记
        return item
