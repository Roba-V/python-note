from lxml import etree

# xpath 解析は「ローカル解析」と「リモート解析」の２種類ある


tree = etree.parse('sample_17.html')

"""
//:
/ :
"""

# ul > li
li_list = tree.xpath('//ul/li/text()')

print(li_list)
print(len(li_list))

# id 属性を持つ li タグ
li_list = tree.xpath('//ul/li[@id]/text()')
print(li_list)
print(len(li_list))

# id=tokyo の li タグ
li_list = tree.xpath('//ul/li[@id="tokyo"]/text()')
print(li_list)
print(len(li_list))

# id=tokyo の li タグの class の値
li_list = tree.xpath('//ul/li[@id="tokyo"]/@class')
print(li_list)
print(len(li_list))

# マッチ
li_list = tree.xpath('//ul/li[contains(@id, "c")]/text()')
print(li_list)
print(len(li_list))

# c から始まる id の li タグ
li_list = tree.xpath('//ul/li[starts-with(@id, "c")]/text()')
print('*' * 10)
print(li_list)
print(len(li_list))

# and 演算
li_list = tree.xpath('//ul/li[@id="tokyo" and @class="right"]/text()')
print(li_list)
print(len(li_list))

# | 演算
li_list = tree.xpath(
    '//ul/li[@id="osaka" ]/text() | //ul/li[@class="right"]/text()')
print(li_list)
print(len(li_list))
