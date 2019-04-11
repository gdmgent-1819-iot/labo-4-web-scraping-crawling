import scrapy

class Flipkart(scrapy.Sider):
    name = 'flippy'
    start_urls = ['https://www.flipkart.com/mobile-phones-store']

    def parse(self,response):
        for phone in response.css('a.K6IBc-.required-tracking'):
            yield{
                'phone name':phone.css('div.iUmrbN::text').extract_frist(),
                'price':phone.css('div.3o3r66::text').extract_frist(),
            }