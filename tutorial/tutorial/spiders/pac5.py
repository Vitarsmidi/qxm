#!/usr/bin/env python
# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By

import scrapy
from MtimeSpider.items import MtimespiderItem

page_no = 0


class MovieSpiderSpider(scrapy.Spider):
    # 定义spider的名字
    name = 'movie_spider'
    # 爬取的域名
    allowed_domains = ['www.mtime.com']
    # 从哪个页面开始
    start_urls = ['http://www.mtime.com/top/movie/top100/']

    def parse(self, response):
        global page_no
        # 爬取所有电影元素
        movie_list = response.xpath('//ul[@id="asyncRatingRegion"]/li')
        for movie_li in movie_list:
            item = MtimespiderItem()
            # 电影介绍页面的url
            item['url'] = movie_li.xpath('div[@class="mov_pic"]/a/@href').extract_first()
            # 电影图片的url
            item['img_url'] = movie_li.xpath('div[@class="mov_pic"]/a/img/@src').extract_first()
            # 电影标题
            item['title'] = movie_li.xpath('div[@class="mov_con"]/h2/a/text()').extract_first()
            # 电影导演
            item['directors'] = movie_li.xpath('div[@class="mov_con"]/p')[0].xpath('./a/text()').extract()
            if len(movie_li.xpath('div[@class="mov_con"]/p')) == 4:
                # 电影主演
                item['actors'] = movie_li.xpath('div[@class="mov_con"]/p')[1].xpath('./a/text()').extract()
                # 电影简介
                item['description'] = movie_li.xpath('div[@class="mov_con"]/p')[3].xpath("./text()").extract_first()
            else:
                # 电影主演
                item['actors'] = ''
                # 电影简介
                item['description'] = movie_li.xpath('div[@class="mov_con"]/p')[2].xpath("./text()").extract_first()
            # 电影得分
            item['mark'] = ''.join(movie_list[0].xpath('div[@class="mov_point"]/b/span/text()').extract())
            # 电影得分信息
            item['mark_info'] = movie_li.xpath('div[@class="mov_point"]/p/text()').extract_first()
            yield item

        page_no += 1
        if page_no <= 9:
            # 获取下一页的链接
            new_link = response.xpath('//div[@id="PageNavigator"]/a')[page_no].xpath('./@href').extract_first()
            # 再次请求下一个页面
            yield scrapy.Request(new_link, callback=self.parse)