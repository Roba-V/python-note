import json

import requests

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/'
                  '537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.'
                  '36'
}

data = {
    'kw': 'eye'
}

response = requests.post(url, data, headers=headers)

content = response.text

obj = json.loads(content)

print(obj)
