import requests
from pyquery import PyQuery as pq

url = 'http://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}
html = requests.get(url, headers=headers).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
print(items)
for item in items:
    questions = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()

    # 方法1
    file = open('explore.txt', 'a', encoding='utf-8')
    file.write('\n'.join([questions, author, answer]))
    file.write('\n' + '=' * 50 + '\n')
    file.close()

    # 方法2
    # with open('explore.txt', 'a', encoding='utf-8') as file:
    #     file.write('\n'.join([questions, author, answer]))
    #     file.write('\n' + '=' * 50 + '\n')