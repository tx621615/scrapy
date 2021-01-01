# 获得中国大学排名并且进行输
"""
实现requests库和beautifulsoup库的综合使用
requests库只是用来获得html文档
beautifulsoup库用来解析文档
解析常用的方法一个是获得某个标签下的子标签或者孙子标签，以及遍历标签
            一个是返回子标签中的所有标签
中文对齐的解决（字符串格式化问题）
"""
import requests
from bs4 import BeautifulSoup
import bs4

# 定义三个结构函数

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    count = 0
    for tr in soup.find('tbody').children:         # 从tbody中获取每一行，从每一行中获取所有td（单元格），从单元格中读取标签内容
        print(tr)
        count += 1
        if count == 13:
            continue
        if isinstance(tr, bs4.element.Tag):         # 注意字符串类型也可能是孩子，即孩子可能并不是子标签。所以要类型判断一下
            tds = tr.find_all("td")                 # 找到所有标签
            ulist.append([tds[0].string, tds[1].string, tds[2].string])     # 加入二维数组



def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))  # 中文不对齐是因为使用西文空格进行填充，改成中文空格就可以了



def main():
    uinfo = []
    url = "https://www.dxsbb.com/news/46702.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 18)  # 13行不清楚为什么打印不了,可能是因为有的td中嵌入了<a>，所以打印不了


main()