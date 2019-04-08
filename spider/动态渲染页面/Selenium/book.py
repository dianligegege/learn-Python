from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
import pymysql

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
keyword = 'JavaScript'

# 链接Mysql
db = pymysql.connect(host='localhost', user='root', password='880508', port=3306)
cursor = db.cursor()

def index_page(page):
    print('正在爬取',page,'页')
    try:
        url = 'https://book.douban.com/tag/' + quote(keyword)
        browser.get(url)
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.subject-item'))
        )
        nextPage = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.next'))
        )
        get_products()
        if page < 3:
            nextPage.click()
    except TimeoutException:
        index_page()
            
# 解析html,获取图书信息
def get_products():
    html = browser.page_source
    # 要配置parse，否则无法用标签选择器
    doc = pq(html, parser="html")
    items = doc('.subject-list .subject-item').items()
    print(items)
    for item in items:
        product = {
            'name': item.find('.info a').text(),
            'writer': item.find('.info>.pub').text(),
            'score': item.find('.info>.star .rating_nums').text(),
            'people': item.find('.info>.star .pl').text(),
            'info': item.find('.info>p').text(),
            'image': item.find('.pic>.nbg img').attr('src'),
        }
        saveProduct(product)

# 保存数据到Mysql
def saveProduct(product):
    print(product)
    table = 'books'
    keys = ','.join(product.keys())
    values = ','.join(["%s"] * len(product))
    sql3 = 'INSERT INTO books (name) VALUES (%s)'
    cursor.execute(sql3, 'zhanli')
    db.commit()
    # sql2 = 'INSERT INTO {table} ({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
    # try:
    #     if cursor.execute(sql2, tuple(product.values())):
    #         print('success')
    #         db.commit()
    # except:
    #     print('failes')
    #     db.rollback()

maxPage = 3
def main():
    for i in range(1, maxPage+1):
        index_page(i)
    db.close()

main()