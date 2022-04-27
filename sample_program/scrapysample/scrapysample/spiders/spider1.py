import scrapy


class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response, **kwargs):
        with open('index.html', 'w') as html_file:
            html_file.write(response.text)
