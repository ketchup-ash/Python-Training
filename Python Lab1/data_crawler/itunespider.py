from scrapy import Spider

class ItunesSpider(Spider):

    name = 'itunes'
    start_urls = [
        'https://www.apple.com/in/itunes/charts/songs/'
    ]

    def parse(self, response):

        songs = response.css('.chart-grid .section-content ul li')

        for item in songs:
            yield {
                'title':item.css('h3 a::text').extract_first(),
                'artist':item.css('h4 a::text').extract_first(),
                'rank':item.css('strong::text').extract_first().replace('.',''),
                'link':item.css('h3 a::attr(href)').extract_first(),
                'imgsrc':item.css('img::attr(src)').extract_first(),
            }