# 从html格式中提取信息
import requests
from bs4 import BeautifulSoup
url = "http://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))       # 直接使用属性名没有作用，只能通过attrs返回属性名和属性值的字典
