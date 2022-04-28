import urllib.request

url = 'https://movie.douban.com/j/chart/top_list' \
      '?type=17&interval_id=100:90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/'
                  '537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.'
                  '36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')
print(content)

# データをダウンロード
with open('douban.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
