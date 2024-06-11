import scrapy


class LampnewparsSpider(scrapy.Spider):
    name = "lampnewpars"
    allowed_domains = ["https://www.divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lamps = response.css('div._Ud0k')
        for lamp in lamps:
            yield {
                'name': lamp.css('div.lsooF span::text').get(),
                'price': lamp.css('div.q5Uds span::text').get(),
                'url': lamp.css('a').attrib['href']
            }


