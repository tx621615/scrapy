# 通过beautifulsoup库来解析HTML源代码,注意库简写为bs4,其中有一个类就是BeautifulSoup
from bs4 import BeautifulSoup
import requests
url = "http://python123.io/ws/demo.html"
r = requests.get(url)
print(r.text)
demo = r.text
# 实用BeautifulSoup来解析HTML文件，使其表现的更加易读
soup = BeautifulSoup(demo, 'html.parser')  # BeautifulSoup的构造方法形成一个对象保存HTML文档
print(soup.prettify())  # 对齐非常工整