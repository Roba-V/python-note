import requests

url = 'https://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/'
                  '537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.'
                  '36'
}

data = {
    'wd': '北京'
}

response = requests.get(url, data, headers=headers)

content = response.text

print(content)
