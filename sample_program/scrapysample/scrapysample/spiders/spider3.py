import scrapy

from ..items import ScrapysampleItem


class Spider3Spider(scrapy.Spider):
    name = 'spider3'
    allowed_domains = ['category.dangdang.com']
    start_urls = ['https://category.dangdang.com/cp01.01.00.00.00.00.html']

    base_url = 'https://category.dangdang.com/pg'
    page = 1

    def parse(self, response):
        # piplines  データをダウンロードする
        # items     データ構造を定義
        li_list = response.xpath('//ul[@id="component_59"]/li')

        print('=' * 100)

        for li in li_list:
            src = li.xpath('.//img/@data-original').extract_first()
            if not src:
                src = li.xpath('.//img/@src').extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath(
                './/p[@class="price"]/span[1]/text()').extract_first()
            print(src, name, price)

            book = ScrapysampleItem(src=src, name=name, price=price)

            yield book

        if self.page < 100:
            self.page = self.page + 1
            url = self.base_url + str(self.page) + '-cp01.01.00.00.00.00.html'

            # GET 通信
            yield scrapy.Request(url=url, callback=self.parse)
