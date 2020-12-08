# 利用BS4来对HTML标签树进行遍历
# 遍历分为下行，上行，平行遍历
from bs4 import BeautifulSoup
import requests
url = "http://python123.io/ws/demo.html"
r = requests.get(url)
"""
下行遍历
1.tag.contents--获得该标签所有子节点的列表
2.tag.children--获得子节点的迭代器，可以用于for in
3.tag.descendants--获得该标签子孙结点的迭代器，包含子孙结点用于for in

上行遍历
1.tag.parent --找到该标签的父标签
2.tag.parents -- 节点先辈标签的迭代类型，用于循环遍历先辈节点

平行遍历
1.next_sibling 返回按照HTML文本顺序的下一个平行节点标签
2.previous_sibling 返回按照HTML文本顺序的上一个平行节点标签
3.next_siblings 迭代类型，返回按照HTML文本顺序的后续所有平行节点标签
4.previous_siblings 迭代类型，返回按照HTML文本顺序的前续所有平行节点标签
note:必须是同一个父标签下的才构成兄弟结点，同时尽管是以标签树的形式组织树结构，但是实际上标签中的内容也会形成兄弟结点，需要区分
"""


# 下行遍历

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.head)
print(soup.head.contents)
print(soup.body.contents)  # 注意不仅仅是子标签会作为列表元素，还可能会加入\n元素
print(len(soup.body.contents))
# 可以使用列表的相关方法来访问某个子标签
print(soup.body.contents[1])
# 其他两种迭代器方法不具体细述，比较简单

print("\n-------------------------------------------\n")

# 上行遍历
print(soup.title.parent)
print(soup.html.parent)  # html标签的父标签是其自身
print(soup.parent)  # None,soup标签的父标签是None
# 遍历一个标签的所有先辈,注意最后一定会遍历到soup标签
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

print("\n-------------------------------------------\n")


# 平行遍历
print(soup.a.next_sibling)  # and标签内容，实际中兄弟结点不一定是标签
print(soup.a.next_sibling.next_sibling)
print(soup.a.previous_sibling)  # Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
print(soup.a.previous_sibling.previous.sibling)  # None，没有前面时候就返回None