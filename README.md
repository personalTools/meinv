# meinv
自动下载桌面背景图吧



mzitu
pipelines.py

class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
            "referer":"https://www.mzitu.com"
        }
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url,headers=headers,meta={"image_name":item["image_name"]})


    def file_path(self, request, response=None, info=None):
        file_name = request.meta["image_name"].strip().replace(r'\r\n\t\t',r'').replace(r'/',r'_')
        return 'meimv2/'+file_name+'.jpg'
        
这个headers很重要呦
