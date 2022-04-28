import urllib.parse
import urllib.request

from lxml import etree


def create_request(arg_page):
    url = 'https://sc.chinaz.com/tupian/fengjingtupian.html' \
        if arg_page == 1 \
        else f'https://sc.chinaz.com/tupian/fengjingtupian_{arg_page}.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWeb'
                      'Kit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Saf'
                      'ari/537.36'
    }

    return urllib.request.Request(url=url, headers=headers)


def get_content(arg_request):
    response = urllib.request.urlopen(arg_request)
    return response.read().decode('utf-8')


def down_load(arg_content):
    tree = etree.HTML(arg_content)
    name_list = tree.xpath('//div[@id="container"]//a/img/@alt')
    # 画像のロードがレイジー
    src_list = tree.xpath('//div[@id="container"]//a/img/@src2')
    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src
        urllib.request.urlretrieve(url=url, filename='books/' + name + '.jpg')


if __name__ == '__main__':
    start_page = int(input('取得開始のページ番号を入力してください'))
    end_page = int(input('取得終了のページ番号を入力してください'))

    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        down_load(content)
