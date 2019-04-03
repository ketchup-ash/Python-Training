from scrapy import Spider

class AzlyricsSpider:

    start_url = ["https://www.azlyrics.com/"]

    def parse(self, response):
        songs = response.css('')