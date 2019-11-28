# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from olx_scraper.items import OlxScraperItem

class OlxSpider(CrawlSpider):
    name = "olx_spider"
    allowed_domains = ["pb.olx.com.br"]
    start_urls = [
            'https://pb.olx.com.br/autos-e-pecas/motos',
            'https://pb.olx.com.br/paraiba/joao-pessoa/jardim-oceania/imoveis'
            ]
    rules = (
            Rule(LinkExtractor(allow=(),restrict_css=('.next',)),
                callback="parse_item",
                #follow=False),
                #follow=False),
                follow=True),
            )
    def parse_item(self, response):
        print('Processing ... ' + response.url)
        #item_links = response.css('.large > .detailsLink::attr(href)').extract()
        #for a in item_links:
        #    yeld scrapy.Request(a, callback=self.parse_detail_page)
