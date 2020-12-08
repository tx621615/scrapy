# 更好的方便人阅读html以及方便程序分析---prettify()方法
"""
prettify()为HTML文本<>及其内容增加'\n'
prettify()可用于标签，方法：<tag>.prettify()
bs4使用的是utf-8编码，py3也是使用utf-8编码
"""
import requests
from bs4 import BeautifulSoup
url = "http://python123.io/ws/demo.html"
r = requests.get(url)
print(r.text)  # 注意通过idle显示的r.text相比Html源码会再每行末尾添加\r\n，实际上就是将Html解释成string

# prettify方法的演示
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
# 对标签的操作
print(soup.a.prettify())