# findall方法基本使用以及正则表达式的使用
import requests
from bs4 import BeautifulSoup
import re  #正则表达式的库
'''
<>.find_all(name, attrs, recursive, string, **kwargs)
    find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件.
name:查找的标签名字
attrs: 对标签属性值(不是属性名)的检索字符串，可标注属性检索
recursive: 是否对子孙(False表示仅对孩子结点检索)全部检索，默认True
string: <>…</>中字符串区域的检索字符串
简便写法：
<tag>(..) 等价于 <tag>.find_all(..)
soup(..) 等价于 soup.find_all(..)
**kwargs：找某个标签的属性键值对
'''
url = "http://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')

# 返回soup标签（根标签）下a标签的所有信息,以列表形式返回
print(soup.find_all('a'))
# 同时查找多个标签---通过列表表示
print(soup.find_all(['a', 'b']))
# 查找所有标签,name = True
# print(soup.find_all(True))

# 可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag:
print(soup.find_all('p', attrs='course'))   # 对标签属性值过滤，这是不考虑属性名的形式，可能会出现问题
# 查找含有某个属性值对的标签
# print(soup.find_all('a', attrs='link1')) #  只查属性值可能查不到
print(soup.find_all('a', attrs={'id' : 'link1'}))   # 键值对一起查找
# 使用正则表达式进行模糊查询
print(soup.find_all(id='link'))
print(soup.find_all(id=re.compile('link')))

# 检索标签内容
print(soup.find_all(string='Basic Python'))  # 精确查找某一个字符串---一个问题是你必须知道是否有该值，只能判断是否存在
print(soup.find_all(string=re.compile('python')))   # 使用字符串模糊查找--正则表达式