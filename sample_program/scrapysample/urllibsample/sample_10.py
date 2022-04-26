import urllib.parse
import urllib.request


def create_request(arg_page):
    base_url = 'https://movie.douban.com/j/chart/top_list' \
               '?type=17&interval_id=100:90&action=&'
    data = {
        'start': (arg_page - 1) * 20,
        'limit': 20
    }
    data = urllib.parse.urlencode(data)
    url = base_url + data
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWeb'
                      'Kit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Saf'
                      'ari/537.36'
    }

    return urllib.request.Request(url=url, headers=headers)


def get_content(arg_request):
    response = urllib.request.urlopen(arg_request)
    return response.read().decode('utf-8')


def down_load(arg_page, arg_content):
    with open('douban_' + str(arg_page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(arg_content)


if __name__ == '__main__':
    start_page = int(input('取得開始のページ番号を入力してください'))
    end_page = int(input('取得終了のページ番号を入力してください'))

    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        down_load(page, content)
