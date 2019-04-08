import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.get('https://www.python.org')

# 后退前进
browser.back()
time.sleep(1)
browser.forward()

# cookie操作
print(browser.get_cookies())
# 添加cookie
# 一次设一条，包含value等
browser.add_cookie({'name':'zhangli', 'domain':'.python.org', 'value':'genji'})
print(browser.get_cookies())
# 删除cookie
browser.delete_all_cookies()
print(browser.get_cookies())

browser.close()