import urllib.request

from lxml import etree

url = 'http://www.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWeb'
                  'Kit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Saf'
                  'ari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

# Handler オブジェクトを取得
handler = urllib.request.HTTPHandler()

# Opener オブジェクトを取得
opener = urllib.request.build_opener(handler)

# open メソッドを呼び出し
response = opener.open(request)

content = response.read().decode('utf-8')

tree = etree.HTML(content)

result = tree.xpath("//span[@class='bg s_btn_wr']/input[@id='su']/@value")[0]

print(result)
