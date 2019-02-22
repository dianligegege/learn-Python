import requests

# 获取cookie
r = requests.get("https://www.zhihu.com")
print(r.cookies)

for key, value in r.cookies.items():
    print(key + '=' + value)

# 使用cookies登录,在headers中直接加cookie
headers = {
    'Cookie': '_zap=95780700-1af0-47d5-9dba-9011981ca6e6; d_c0="ACCkuWGe2w6PTt30sCD3sQHkakmpWRq4Dak=|1548036528"; q_c1=8600aaa34cb14d3abc686e3d8b8279bb|1548036530000|1548036530000; capsion_ticket="2|1:0|10:1548315198|14:capsion_ticket|44:ZDgyZmYxZDdiMWU3NDE1YzhiYjNmZjE2YTAyZDc5ODk=|da2c984b53e5ff0c2eb59f4c74753286169d56ce753e87a83daeba12cd0e0066"; z_c0="2|1:0|10:1548315199|4:z_c0|92:Mi4xakJfbUFRQUFBQUFBSUtTNVlaN2JEaVlBQUFCZ0FsVk5QN2cyWFFDTjIwU2NqdnBIS29GUS1UVXRaLTBQQWhWYlRB|8df5fd4124046748facb8cf247b8a0afdf7e100e280cd8abbc17e70d2c46b2e8"; tst=r; _xsrf=8fe37897-5362-4574-9f0a-5f428d9495ac; __utmc=51854390; __utmv=51854390.100-1|2=registration_date=20150724=1^3=entry_date=20150724=1; __utma=51854390.1534883143.1550572143.1550572143.1550575070.2; __utmz=51854390.1550575070.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/inbox; tgw_l7_route=4860b599c6644634a0abcd4d10d37251',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
}
r1 = requests.get('https://www.zhihu.com', headers=headers)
# print(r1.text)

# 使用cookie登录，构建RequestCookieJar对象
cookies = '_zap=95780700-1af0-47d5-9dba-9011981ca6e6; d_c0="ACCkuWGe2w6PTt30sCD3sQHkakmpWRq4Dak=|1548036528"; q_c1=8600aaa34cb14d3abc686e3d8b8279bb|1548036530000|1548036530000; capsion_ticket="2|1:0|10:1548315198|14:capsion_ticket|44:ZDgyZmYxZDdiMWU3NDE1YzhiYjNmZjE2YTAyZDc5ODk=|da2c984b53e5ff0c2eb59f4c74753286169d56ce753e87a83daeba12cd0e0066"; z_c0="2|1:0|10:1548315199|4:z_c0|92:Mi4xakJfbUFRQUFBQUFBSUtTNVlaN2JEaVlBQUFCZ0FsVk5QN2cyWFFDTjIwU2NqdnBIS29GUS1UVXRaLTBQQWhWYlRB|8df5fd4124046748facb8cf247b8a0afdf7e100e280cd8abbc17e70d2c46b2e8"; tst=r; _xsrf=8fe37897-5362-4574-9f0a-5f428d9495ac; __utmc=51854390; __utmv=51854390.100-1|2=registration_date=20150724=1^3=entry_date=20150724=1; __utma=51854390.1534883143.1550572143.1550572143.1550575070.2; __utmz=51854390.1550575070.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/inbox; tgw_l7_route=4860b599c6644634a0abcd4d10d37251'
jar = requests.cookies.RequestsCookieJar()
headers = {
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
}
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
r2 = requests.get("http://zhihu.com", cookies=jar, headers=headers)
print(r2.text)