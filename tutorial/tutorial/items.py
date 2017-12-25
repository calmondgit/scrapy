# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BTItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()      #片名
    year = scrapy.Field()       #年代
    classify = scrapy.Field()   #类别
    IMDb = scrapy.Field()       #IMDB
    douban = scrapy.Field()     #豆瓣
    
    
