# -*- coding: utf-8 -*-
import scrapy


class MeituSpider(scrapy.Spider):
    name = 'meitu'
    allowed_domains = ['m.mmonly.cc']
    start_urls = ['https://m.mmonly.cc/mmtp/xgmn/318949.html']

    def parse(self, response):
        image_urls = response.xpath('//div[@class="ArticleImageBox"]/p/a/img/@src').extract()
        image_name = response.xpath('string(//h1)').extract_first()
        yield {
            "image_urls":image_urls,
            "image_name":image_name
        }

        next_url = response.xpath('//div[@class="article_page"]/ul/li[3]/a/@href').extract_first()
        if next_url.find('.html') != -1:
            new_url = 'https://m.mmonly.cc/mmtp/xgmn/{}'.format(next_url)
            yield scrapy.Request(new_url,callback=self.parse)
