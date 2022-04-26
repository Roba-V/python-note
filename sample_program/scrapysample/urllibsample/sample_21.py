# post メソッドで通信

import json
import urllib.request

import jsonpath

url = 'https://dianying.taobao.com/cityAction.json' \
      '?activityId&_ksTS=1650981039792_97' \
      '&jsoncallback=jsonp98&action=cityAction&n_s=new' \
      '&event_submit_doGetAllRegion=true'

headers = {
    'accept': ' text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'accept-language': ' ja,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'cookie': ' t=4c83b3f33c25d5257d2873c51054ab6d; cookie2=179fc87dcfa1cd6def99ab8ec0e4df8f; v=0; _tb_token_=536e4b5071f35; cna=sPc6Gr/xXTsCAYXKUIbG48iF; xlly_s=1; tb_city=110100; tb_cityName="sbG+qQ=="; tfstk=cXuOB3VLHBCT0uPKacKngieb_WOlZaJYd1wckqeaj-xR1V7Ai_3oyOEBfSwzBBC..; l=eBQJHQfqLFVAMDnfBOfwhurza77OHIRfguPzaNbMiOCP_l5H5wjcW6qlKm8MCnMNHs96S3J8Iu2zBJ8GxPlRVcYON7h1WnXI3dC..; isg=BCAgnZXjVgSuUuoApQ3dslz38SjyKQTzD4IMspoxkjvOlcG_RDr1g79jKSUVJbzL',
    'referer': 'https://dianying.taobao.com/?spm=a1z21.3046609.city.1.32c0112alfQxKp&city=110100',
    'sec-ch-ua': ' " Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': ' ?0',
    'sec-ch-ua-platform': ' "macOS"',
    'sec-fetch-dest': ' empty',
    'sec-fetch-mode': ' cors',
    'sec-fetch-site': ' same-origin',
    'user-agent': ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'x-requested-with': ' XMLHttpRequest',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

content = content.split('(')[1].split(')')[0]

with open('sample_21.json', 'w', encoding='utf-8') as f:
    f.write(content)

obj = json.load(open('sample_21.json', 'r', encoding='utf-8'))

city_list = jsonpath.jsonpath(obj, '$..regionName')

print(city_list)
