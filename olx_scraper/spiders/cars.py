# -*- coding: utf-8 -*-
import scrapy
from time import sleep


class CarsSpider(scrapy.Spider):

    name = 'cars'
    allowed_domains = ['pb.olx.com.br']
    start_urls = ['https://pb.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios']


    def parse(self, response):
        self.log('================================= CABEÇALHO - INÍCIO ======================================')
        self.log('Visitei página: %s' % response.url)
        self.log('=================================== CABEÇALHO - FIM ========================================')

        title_site = response.xpath('//title/text()').extract_first()
        self.log('================================= CABEÇALHO - INÍCIO ======================================')
        self.log('Cujo seu título é: %s' % title_site)
        self.log('=================================== CABEÇALHO - FIM ========================================')

        items = response.xpath(
            '//ul[@id="main-ad-list"]/li[not(contains(@class, "list_native"))]'
        )
        self.log('================================= CABEÇALHO - INÍCIO ======================================')
        self.log('=============== VISUALIZANDO TODOS OS ANÚNCIOS DE CARROS  ===============')
        self.log('QUANTIDADE DE ANÚNCIOS POR PÁGINA: %s'% len(items))
        self.log('=================================== CABEÇALHO - FIM ========================================')
        for item in items:
            url = item.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_detail)
        next_page = response.xpath(
            '//div[contains(@class, "module_pagination")]//a[@rel = "next"]/@href'
        )
        if next_page:
            #pass
            self.log('Próxima Página: {}'.format(next_page.extract_first()))
            yield scrapy.Request(
                url=next_page.extract_first(), callback=self.parse
            )

    def parse_detail(self, response):
        title = response.xpath('//title/text()').extract_first()

        year = response.xpath(
            "//div[contains(span, 'Ano')]")[0].css('a::text'
            ).get()

        try:
            color = response.xpath("//div[contains(span, 'Cor')]")[0].css('span::text')[1].get()
        except IndexError:
            color = "N/A"
        try:
            doors = response.xpath("//div[contains(span, 'Portas')]")[0].css('span::text')[1].get()
        except IndexError:
            doors = "N/A"

        try:
            fuel = response.xpath("//div[contains(span, 'Combustível')]")[0].css('a::text').get()
        except IndexError:
            fuel = "N/A"

        try:
            mileage = response.xpath("//div[contains(span, 'Quilometragem')]")[0].css('span::text')[1].get()
        except IndexError:
            mileage = "N/A"

        try:
            transmission = response.xpath("//div[contains(span, 'Câmbio')]")[0].css('span::text')[1].get()
        except IndexError:
            transmission = "N/A"

        try:
            zip_code = response.xpath("//div[contains(@data-testid, 'ad-properties')]").xpath("*[contains(., dd)]")[0].css('dd::text').get()
        except:
            zip_code = "N/A"

        try:
            city = response.xpath("//div[contains(@data-testid, 'ad-properties')]").xpath("*[contains(., dd)]")[1].css('dd::text').get()
        except:
            city = "N/A"

        try:
            city_block = response.xpath("//div[contains(@data-testid, 'ad-properties')]").xpath("*[contains(., dd)]")[2].css('dd::text').get()
        except:
            city_block = "N/A"

        county = response.xpath(
            "//span[contains(text(), 'Município')]/following-sibling::strong/a/@title"
            ).extract_first()

        self.log('=============== VISUALIZANDO DETALHES DO CARRO  ===============')
        yield {

            'title': title,
            'year': year, 'color': color,
            'doors': doors,
            'fuel': fuel,
            'mileage': mileage,
            'transmission': transmission,
            'zip_code': zip_code,
            'city': city,
            'city_block': city_block,
        }
        car = {}
        car['title'] = title
        car['year'] = year
        car['color'] = color
        car['doors'] = doors
        car['fuel'] = fuel
        car['mileage'] = mileage
        car['transmission'] = transmission
        car['zip_code'] = zip_code
        car['city'] = city
        car['city_block'] = city_block
        print(car)
        sleep(2)
