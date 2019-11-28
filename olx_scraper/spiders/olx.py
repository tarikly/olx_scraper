# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from olx_scraper.items import OlxScraperItem
from time import sleep

class OlxSpider(CrawlSpider):
    name = "olx_spider"
    allowed_domains = ["pb.olx.com.br"]
    start_urls = [
            #'https://pb.olx.com.br/autos-e-pecas/motos',
            'https://pb.olx.com.br/paraiba/joao-pessoa/jardim-oceania/imoveis'
            ]
    rules = (
            Rule(LinkExtractor(allow=(),#restrict_css=('.next',)
                ),
                callback="parse_item",
                follow=False),
                #follow=False),
                #follow=True),
            )
    #scrapy.Request(response.css('.page_listing .grid-col .col-2 .OLXad-list-title'))
    #response.css('.page_listing .grid-col .col-3 .OLXad-list-price').getall()
    #response.css('.page_listing .section_OLXad-list .item .OLXad-list-link::attr(title)').get()
    #response.css('.page_listing .section_OLXad-list .item .OLXad-list-link::attr(href)').get()
    #response.css('.page_listing .section_OLXad-list .item .col-1 .OLXad-list-image .OLXad-list-image-box .image::attr(src)').getall()
    #response.css('.page_listing .section_OLXad-list .item').extract()[0]

    def parse_item(self, response):
        print('Processing ... ' + response.url)
        for ad in response.css('.page_listing .section_OLXad-list .list .item'):
            anuncio = OlxScraperItem()
            anuncio['ad_id'] = ad.css('.OLXad-list-link::attr(id)').get()
            anuncio['vendor_id'] = ad.css('.item::attr(data-account_id)').get()
            anuncio['title'] = ad.css('.OLXad-list-link::attr(title)').get()
            anuncio['price'] = ad.css('.OLXad-list-price').get()
            anuncio['url'] = ad.css('.OLXad-list-link::attr(href)').get()
            print(anuncio)
            sleep(2)

