# 使用Beautiful类解析整个HTML文档，主要是根据标签解析
# 为什么使用BeautifulSoup保存整个HTML文档，因为其提供的方法可以帮助我们按标签解析HTML，而直接返回的内容只是HTML文档的string表示没有提供方法具体分析
"""
1.Tag
2.Tag.name
3.Tag.attrs
4.Tag.string
5.Tag.string----Comment note:注释依然通过string获得，通过string获得内容时可能获得标签内的注释内容，其类型与内容类型是不同的，同时其!--等标签提示被删除，某些时候可能需要区分
总结所有方法均需要先获得一个标签对象
"""

from bs4 import BeautifulSoup
import requests
url = "http://python123.io/ws/demo.html"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

# 标签---soup.tag---可以很方便获得标签及其中内容
print(soup.title)
tag = soup.a
print(tag)  # 注意当存在多个相同的tag时，soup.tag返回第一个
print(type(tag))  # <class 'bs4.element.Tag'>
# 标签的名字-- soup.tag.name
print(soup.a.name)
print(soup.a.parent.name)  # parent指父标签（即包含本标签的最近的标签）
print(soup.a.parent.parent.name)
print(type(soup.a.name))  # <class 'str'>

# 标签的属性---tag.attrs--返回的是字典类型字段（属性名：属性值）
tag = soup.a
print(tag.attrs)
print(type(tag.attrs))  # <class 'dict'>
# 访问具体的某个属性---使用字典的访问即可
print(tag.attrs['href'])
print(tag.attrs['class'])

# 标签的内容--tag.string
print(soup.a)
print(soup.a.string)
print(soup.p)
print(soup.p.string)
print(type(soup.p.string))  # 不是基本的string类型， <class 'bs4.element.NavigableString'>

# 标签的注释
newsoup = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>", "html.parser")
print(newsoup.b.string)
print(type(newsoup.b.string))   # <class 'bs4.element.Comment'> note:通过string获得内容时可能获得标签内的注释内容，其类型与内容类型是不同的，同时其!--等标签提示被删除，某些时候可能需要区分
print(newsoup.p.string)
print(type(newsoup.p.string))