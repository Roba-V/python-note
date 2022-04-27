from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions

chrome_options = ChromiumOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

chrome_options.binary_location = '/Applications/Google Chrome.app/' \
                                 'Contents/MacOS/Google Chrome'

path = './chromedriver'

browser = webdriver.Chrome(path, chrome_options=chrome_options)

url = 'https://www.baidu.com'

browser.get(url)

browser.save_screenshot('baidu.png')
