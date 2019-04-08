import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
# 打开标签页
browser.execute_script('window.open()')
# 显示所有打开的标签页
print(browser.window_handles)
# 切换标签
browser.switch_to_window(browser.window_handles[1])
browser.get('https://python.org')

time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://www.zhihu.com')

# 异常处理
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()
