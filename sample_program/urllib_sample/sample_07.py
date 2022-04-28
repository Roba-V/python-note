# post メソッドで通信

import json
import urllib.parse
import urllib.request

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/'
                  '537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.'
                  '36'
}

data = {
    'kw': 'spider'
}

data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=url, data=data, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')
print(content)

obj = json.loads(content)
print(obj)
