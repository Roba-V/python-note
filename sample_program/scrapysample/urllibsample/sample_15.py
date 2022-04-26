import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWeb'
                  'Kit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Saf'
                  'ari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

proxies = {
    'http': '106.54.128.253:999'

}

# Handler オブジェクトを取得
handler = urllib.request.ProxyHandler(proxies=proxies)

# Opener オブジェクトを取得
opener = urllib.request.build_opener(handler)

# open メソッドを呼び出し
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)

with open('daili.html', 'w', encoding='utf-8') as f:
    f.write(content)
