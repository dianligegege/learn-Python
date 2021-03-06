from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)

# 获取属性
print(logo.get_attribute('class'))

# 获取文本值
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)

# 获取 id、位置、 标签名和大小
print(input.id)
print(input.location) # 相对位置
print(input.tag_name)
print(input.size)
