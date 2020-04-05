# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline

class TupianPipeline(object):
    def process_item(self, item, spider):
        return item

class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url,meta={"image_name":item["image_name"]})


    def file_path(self, request, response=None, info=None):
        file_name = request.meta["image_name"].strip().replace(r'\r\n\t\t',r'').replace(r'/',r'_')
        return 'meimv/'+file_name+'.jpg'
