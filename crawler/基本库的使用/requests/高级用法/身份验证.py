import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1

r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
# 或者直接写
r = requests.get('http://localhost:5000', auth=('username', 'password'))
# 或者使用OAuth认证
url = 'https://api.twitter.com/1.1/acount/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
requests.get(url, auth=auth)
