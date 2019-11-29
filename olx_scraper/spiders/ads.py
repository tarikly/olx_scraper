# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from olx_scraper.items import AdItem
from time import sleep

class AdsSpider(CrawlSpider):
    name = "ads_spider"
    def start_requests(self):
        start_urls = ['https://pb.olx.com.br/autos-e-pecas/motos',]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #print('Processing. ' + response.url)
        #sleep(2)
        #print()
        for ad in response.css('.page_listing .section_OLXad-list .list .item'):
            print('Processing... ' + response.url)
            anuncio = AdItem()
            anuncio['ad_id'] = ad.css('.OLXad-list-link::attr(id)').get()
            anuncio['vendor_id'] = ad.css('.item::attr(data-account_id)').get()
            anuncio['ad_title'] = ad.css('.OLXad-list-link::attr(title)').get()
            anuncio['ad_price'] = ad.css('.OLXad-list-price::text').get()
            anuncio['ad_url'] = ad.css('.OLXad-list-link::attr(href)').get()
            if anuncio['ad_id']:
                print(anuncio)
            sleep(2)

