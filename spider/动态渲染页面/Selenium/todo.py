from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 声明浏览器对象
browser = webdriver.Chrome()

# 访问页面
browser.get('https://stackoverflow.com/')

# 查找节点
input1 = browser.find_element_by_name('q')

input2 = browser.find_element_by_css_selector('.s-input.js-search-field')

selectlist = browser.find_elements(By.CSS_SELECTOR, '.question-summary.narrow')

print(input1)
print(input2)
print(selectlist)

input1.send_keys('python')
time.sleep(1)
input1.clear()
input1.send_keys('javascript')

btn = browser.find_element_by_css_selector('.js-search-submit')
btn.click()

browser.close()
