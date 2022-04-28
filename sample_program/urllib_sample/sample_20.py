import json

import jsonpath

obj = json.load(open('sample_20.json', 'r', encoding='utf-8'))

# 全ての本の作者
author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
print(author_list)

# １冊目の本の作者
author_list = jsonpath.jsonpath(obj, '$.store.book[0].author')
print(author_list)

# 全ての作者
author_list = jsonpath.jsonpath(obj, '$..author')
print(author_list)

# store 配下の全ての要素
tag_list = jsonpath.jsonpath(obj, '$.store.*')
print(tag_list)

# store 配下の全ての price
price_list = jsonpath.jsonpath(obj, '$.store..price')
print(price_list)

# 3冊目の本
book = jsonpath.jsonpath(obj, '$.store.book[2]')
print(book)

# 最後の本
book = jsonpath.jsonpath(obj, '$.store.book[(@.length-1)]')
print(book)

# 最初の２冊
book_list = jsonpath.jsonpath(obj, '$..book[0:2]')
print(book_list)

# isbn がある全ての本
# 条件をつける場合には括弧の前にはてなマークをつける必要がある。
book_list = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
print(book_list)

# 5000円以上の本
book_list = jsonpath.jsonpath(obj, '$..book[?(@price>5000)]')
print(book_list)
