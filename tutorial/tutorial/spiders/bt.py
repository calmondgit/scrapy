# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import BTItem

class BtSpider(scrapy.Spider):
    name = "bt"
    allowed_domains = ["m.btbtt.co"]
    start_urls = [
            'http://m.btbtt.co/forum-index-fid-1183-typeid1-5-typeid2-0-typeid3-0-typeid4-0.htm'
            ]
    
    
  
    
    def parse(self,response):
        
        
        pre_urls = response.xpath('//*[@id="threadlist"]/table/tr/td[1]/a[6]/@href').extract()
            #'//*[@id="threadlist"]/table[1]/tbody/tr/td[1]/a[6]'   no tbody!!
        for pre_url in pre_urls:
            
            yield scrapy.Request(url='http://m.btbtt.co/'+pre_url,callback=self.parse_detail)
        
        
        nexturl = response.xpath('//*[@id="body"]/div/div[3]/a').re(r'\"(.+?)\">▶')[0]
        if nexturl:
            
            yield scrapy.Request(url='http://m.btbtt.co/'+nexturl,callback=self.parse)
       
    def parse_detail(self, response):
        
        
        it= response.xpath('//*[@id="body"]/div/table[2]/tr[1]/td[3]/div[1]/p/text()')
        btitem= BTItem()  
        btitem['title']=it.re(r'译\s+名(.+)').strip()
        btitem['year']=it.re(r'年\s+代\s+(\d{4})')
        btitem['classify']=it.re(r'类\s+别\s+(.+)')
        btitem['IMDb']=it.re(r'IMDb评分\s+(\d\.\d)')
        btitem['douban']=it.re(r'豆瓣评分\s+(\d\.\d)')
        
        yield btitem
      