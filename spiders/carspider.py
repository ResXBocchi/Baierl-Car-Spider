import scrapy


class CarspiderSpider(scrapy.Spider):
    name = 'carspider'
    allowed_domains = ['baierl.com']
    start_urls = ['http://baierl.com/']

    def parse(self, response):
        pass
