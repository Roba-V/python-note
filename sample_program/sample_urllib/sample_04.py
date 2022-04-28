import urllib.request

url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKi'
                  't/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/5'
                  '37.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
