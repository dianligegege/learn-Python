from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')

# 隐式等待
# 1. 找到节点，直接运行
# 2.没有找到，10s后报错
# input = browser.find_element_by_class_name('zu-top-add-question')
# browser.implicitly_wait(10)

# 显式等待
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_all_elements_located((By.ID, 'q')))
btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.message')))

print(input)
print(btn)



