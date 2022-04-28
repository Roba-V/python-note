import requests

url = 'https://www.yahoo.co.jp'

response = requests.get(url=url)

# レスポンスのタイプ
print(type(response))

response.encoding = 'utf-8'
# ソースコード
print(response.text)

print(response.url)

# bytes のソースコード
print(response.content)

print(response.status_code)

print(response.headers)
