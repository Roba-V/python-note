# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import urllib.request


class ScrapysamplePipeline:

    def open_spider(self, spider):
        print('+' * 100)
        self.fp = open('book.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item))

        return item

    def close_spider(self, spider):
        print('-' * 100)
        self.fp.close()


class DownloadImgPipeline:

    def process_item(self, item, spider):
        url = 'http:' + item.get('src')
        filename = './books/' + item.get('name') + '.jpg'

        urllib.request.urlretrieve(url=url, filename=filename)

        return item
