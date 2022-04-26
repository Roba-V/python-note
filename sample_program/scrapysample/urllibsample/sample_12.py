import urllib.error
import urllib.request

url = 'https://blog.csdn.net/sulixu/article/details/1198189491'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWeb'
                  'Kit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Saf'
                  'ari/537.36'
}

try:
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError:
    print('メンテナンス中...')
except urllib.error.URLError:
    print('メンテナンスはまだ終わっていない...')
