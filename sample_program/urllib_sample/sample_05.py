import urllib.parse
import urllib.request

url = 'https://www.baidu.com/s?wd='

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/'
                  '537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.'
                  '36'
}

# 「日本語」の三文字をunicodeに変換
name = urllib.parse.quote('日本語')
url += name

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
