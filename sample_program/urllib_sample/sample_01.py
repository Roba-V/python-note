# urllib で baidu ホームページのソースコードをクローリングする。

import urllib.request

# URL を定義
url = 'http://www.baidu.com'

# ブラウザを真似してサーバにアクセスする。
response = urllib.request.urlopen(url)

# レスポンスの中のページのソースコードを取得する。
# read メソッドの戻り値はバイナリデータになる。
# でコーデする必要がある
content = response.read().decode('utf-8')

# データを表示
print(content)
