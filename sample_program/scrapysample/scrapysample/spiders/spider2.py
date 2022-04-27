import scrapy


class Spider2Spider(scrapy.Spider):
    name = 'spider2'
    allowed_domains = ['www.yahoo.co.jp']
    start_urls = ['https://www.yahoo.co.jp']

    def parse(self, response):
        # content = response.text
        # content = response.body
        print('=====================================')
        # print(content)

        span_list = response.xpath(
            '//section[@id="tabpanelTopics1"]//ul/li//a//h1/span/text()')
        tool_list = response.xpath(
            '//div[@id="ToolList"]//li//p/span/span/text()'
        )

        print(span_list.extract())
        print(tool_list.extract())
