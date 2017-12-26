# -*- coding: utf-8 -*-
import scrapy
from nc.items import NcItem

class NatCommSpider(scrapy.Spider):
    name = "nat_comm"
    allowed_domains = ["https://www.nature.com/ncomms/articles"]
    start_urls = ['http://https://www.nature.com/ncomms/articles/']


    def start_requests(self):
		
        reqs=[]
        for i in range(1,3):
            req=scrapy.Request("https://www.nature.com/ncomms/articles?searchType=journalSearch&sort=PubDate&page=%d"%i)
            reqs.append(req)
		
        return reqs
		
    def parse(self, response):
        
        pre_urls = response.xpath('//*[@id="content"]/div[3]/div/div/div/div[1]/div/ul/li/article/div/h3/a/@href').extract()
        for pre_url in pre_urls:
            
            yield scrapy.Request(url='https://www.nature.com'+pre_url,callback=self.parse_detail)
			
    def parse_detail(self,response):
	
        item = NcItem()
        response.xpath('//*[@id="Abs1-content"]/p/text()')
		#//*[@id="Sec1-content"]/p/text()[1]
		#//*[@id="Abs1"]/span[2]/text()
		#//*[@id="Sec1"]/span[2]/text()
        item['title']       = response.xpath('//*[@id="content"]/div/div/article/div[1]/header/div/h1/text()').extract()
        item['keyword']     = response.xpath('//*[@data-component="article-subject-links"]/li/a/text()').extract()
        item['abstract']    = ''.join(response.xpath('//*[@id="Abs1-content"]/p/text()').extract())
        k = 0
        itemls=['introduction','results','discussion','methods']
        for j in range (1,20):
            con =''.join(response.xpath('//*[@id="Sec%d-content"]/p/text()'%j).extract())
			#''.join(response.xpath('//*[@id="Sec3-content"]/p/text()').extract())
            if con:
                item[itemls[k]]= con
                k +=1
		
        item['additionalInformation'] = response.xpath('//*[@id="additional-information-content"]/p/text()').extract()
        item['url']         = response.url
		
        yield item
		
		
		
		
		
		
		
		
		
		
		
		