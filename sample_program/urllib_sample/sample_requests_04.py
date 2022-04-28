import requests

url = 'https://www.baidu.com/s?'

headers = {
    'User-Agent': ' '.join(['Mozilla/5.0 (Macintosh;',
                            'Intel Mac OS X 10_15_7)',
                            'AppleWebKit/537.36 (KHTML, like Gecko)',
                            'Chrome/100.0.4896.127 Safari/537.36'])
}

data = {
    'wd': 'ip'
}

proxies = {
    'http': '118.163.120.181:58837'
}

response = requests.get(url, data, headers=headers, proxies=proxies)
response.encoding = 'utf-8'

content = response.text

print(content)

with open('1.html', 'w', encoding='utf-8') as f:
    f.write(content)
