# -*- coding: utf-8 -*-
import scrapy
from time import sleep
import js2xml
import lxml.etree
from parsel import Selector
#javascript = response.css('script::text')[4].get()
#xml = lxml.etree.tostring(js2xml.parse(javascript), encoding='unicode')
#selector = Selector(text=xml)


class CarsSpider(scrapy.Spider):

    name = 'ads'
    allowed_domains = ['pb.olx.com.br']
    start_urls = ['https://pb.olx.com.br/autos-e-pecas/motos']


    def parse(self, response):
        print('Processando página: %s' % response.url)
        url_title = response.xpath('//title/text()').get()
        print('Título da página: %s' % url_title)

        items = response.xpath(
            '//ul[@id="main-ad-list"]/li[not(contains(@class, "list_native"))]'
        )
        print('QUANTIDADE DE ANÚNCIOS NA PÁGINA: %s'% len(items))

        for item in items:
            url = item.xpath('./a/@href').get()
            yield scrapy.Request(url=url, callback=self.parse_detail)
        next_page = response.xpath(
            '//div[contains(@class, "module_pagination")]//a[@rel = "next"]/@href'
        )
        if next_page:
            #pass
            self.log('Próxima Página: {}'.format(next_page.get()))
            yield scrapy.Request(
                url=next_page.extract_first(), callback=self.parse
            )

    def parse_detail(self, response):
        javascript = response.css('script::text')[4].get()
        xml = lxml.etree.tostring(js2xml.parse(javascript), encoding='unicode')
        

        print(response.css('script::text')[4].getall())
        sleep(2)

    #scrapyrt - scrapy http api

    def modify_realtime_request(self, request):
        request.meta["dont_redirect"] = True
        return request
