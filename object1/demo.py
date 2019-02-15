# from selenium import webdriver
# browser = webdriver.PhantomJS()
# browser.get('http://www.baidu.com')
# print(browser.current_url)

# from bs4 import BeautifulSoup
# soup = BeautifulSoup('<p>hello</p>')
# print(soup.p.string)

# import tesserocr
# from PIL import Image
# image = Image.open('/gitonject/test.png')
# print(tesserocr.image_to_text(image))

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

if __name__ == "__main__":
    app.run()