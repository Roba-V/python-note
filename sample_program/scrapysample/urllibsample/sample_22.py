from bs4 import BeautifulSoup

# ローカルファイルを解析
soup = BeautifulSoup(open('sample_22.html'), 'lxml')

# 最初の a
print(soup.a)
print(soup.a.name)
print(soup.a.attrs)

print('*' * 10)
# bs4 の関数（３つ）
# find(), find_all(), select()

print(soup.find('a'))
print(soup.find('a', title="a2"))
print(soup.find('a', class_="a1"))

print('-' * 10)

print(soup.find_all('a'))
print(soup.find_all(['a', 'li']))
print(soup.find_all(['a', 'ul']))
print(soup.find_all('li', limit=2))

print('-' * 10)

print(soup.select('a'))
print(soup.select('.a1'))
print(soup.select('#c3'))

print(soup.select('li[id]'))
print(soup.select('li[id="tokyo"]'))

print(soup.select('body li'))
print(soup.select('ul>a'))
print(soup.select('li,a'))

print('*' * 10)

print(soup.select('#osaka')[0].string)
print(soup.select('#osaka')[0].get_text())
print(soup.select('#tokyo')[0].string)
print(soup.select('#tokyo')[0].get_text())

print('-' * 10)

print(soup.select('#osaka')[0].name)
print(soup.select('#tokyo')[0].attrs)

print('-' * 10)

print(soup.select('#tokyo')[0].attrs.get('class'))
print(soup.select('#tokyo')[0].get('class'))
print(soup.select('#tokyo')[0]['class'])
