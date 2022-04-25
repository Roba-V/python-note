import urllib.request

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url)

# 一つの型と六つのメソッド
print(type(response))  # HTTPResponse

# 1バイトずつを読み込み
# content = response.read()
# print(content)

# バイト数を指定
# content = response.read(5)
# print(content)

# 一行ごとに読み込み
# content = response.readline()
# print(content)

# 1行ずつ最後まで読み込み
# content = response.readlines()
# print(content)

# ステータスコードを取得
print(response.getcode())

# url を取得
print(response.geturl())

# ヘッダー（ステータス情報）を取得
print(response.getheaders())
