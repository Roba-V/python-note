import urllib.request

url = 'https://weibo.cn/6451491586/info'

headers = {
    'cookie': '???',
    'referer': 'https://weibo.cn/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWeb'
                  'Kit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Saf'
                  'ari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

with open('weibo.html', 'w', encoding='utf-8') as f:
    f.write(content)
