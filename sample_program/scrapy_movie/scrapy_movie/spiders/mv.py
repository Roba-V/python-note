import scrapy

from ..items import ScrapyMovieItem


class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['www.dygod.net']
    start_urls = ['https://www.dygod.net/html/gndy/china/index.html']

    def parse(self, response):
        # 1ページ目の名前 と 2ページ目の画像をクローリングする
        a_list = response.xpath('//div[@class="co_content8"]//td[2]//a[2]')

        for a in a_list:
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()

            url = 'https://www.dygod.net' + href

            yield scrapy.Request(url=url, callback=self.parse_second,
                                 meta={'name': name})
            print(name, url)

    def parse_second(self, response):
        name = response.meta['name']
        src = response.xpath('//div[@id="Zoom"]/img[1]/@src').extract_first()

        movie = ScrapyMovieItem(src=src, name=name)

        # パイプに返却
        yield movie
