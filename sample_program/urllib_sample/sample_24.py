from selenium import webdriver

path = './chromedriver'

browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'

browser.get(url)

# ソースコードを取得
content = browser.page_source
# print(content)

# button = browser.find_element_by_id('su')
# print(button)

# button = browser.find_element_by_name('wd')
# print(button)

# button = browser.find_elements_by_xpath('//input[@id="su"]')
# print(button)

# button = browser.find_elements_by_tag_name('input')
# print(button)

# button = browser.find_elements_by_css_selector('#su')
# print(button)

button = browser.find_elements_by_link_text('hao123')
print(button)
