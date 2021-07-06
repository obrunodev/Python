import scrapy

class NikeSpider(scrapy.Spider):
    name = "Nike"

    def start_requests(self):
        urls = [
            'https://www.nike.com.br/air-jordan-4-153-169-211-292150',
            'https://www.nike.com.br/air-jordan-1-infantil-67-80-445-308788'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]