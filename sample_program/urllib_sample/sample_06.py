# 複数の URL パラメータ

import urllib.parse

base_url = 'https://www.baidu.com/s?'

data = {
    'wd': '日本語',
    'location': '日本'
}

new_data = urllib.parse.urlencode(data)

print(new_data)

url = base_url + new_data

print(url)
