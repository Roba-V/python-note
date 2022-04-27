import time

from selenium import webdriver

path = './chromedriver'

browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'

browser.get(url)

# input_tag = browser.find_element_by_id('su')
# print(input_tag.get_attribute('class'))
# print(input_tag.tag_name)
# print(input_tag.text)

time.sleep(2)

input_tag = browser.find_element(value='kw')
input_tag.send_keys('長渕剛')

time.sleep(2)

btn = browser.find_element(value='su')
btn.click()

time.sleep(2)

js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)

time.sleep(2)

next = browser.find_element_by_xpath('//a[@class="n"]')
next.click()

time.sleep(2)

browser.back()

time.sleep(2)

browser.forward()

time.sleep(2)

browser.quit()
