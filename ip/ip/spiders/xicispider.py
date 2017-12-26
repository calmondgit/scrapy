# -*- coding: utf-8 -*-
import scrapy

from xici.items import XiciItem

class XicispiderSpider(scrapy.Spider):
    name = "xicispider"
    allowed_domains = ["http://www.xicidaili.com/nn"]
    start_urls = ['http://http://www.xicidaili.com/nn/']

    def parse(self, response):
        item = XiciItem()
        for each in response.css('#ip_list tr'):
            ip = each.css('td:nth-child(2)::text').extract_first()
            port = each.css('td:nth-child(3)::text').extract_first()
            if ip:
                ip_port = ip + ':' + port
                item['ip_port'] = ip_port
                yield item
