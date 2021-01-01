import requests  # urllib urllib3
from bs4 import BeautifulSoup  # re  lxml(xpath)
import json
import time
import random
import re

desf = open("JD_spider3.txt", 'w+')  # 保存数据到文件


#建立一个user-Agent池防屏蔽
user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
            'Opera/8.0 (Windows NT 5.1; U; en)',
            'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
            'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0) ']
#随机生成一个headers
user_agent = random.choice(user_agents)
h = {"User-Agent": "Mozilla/5.0"}  # 模拟人类访问行为

count_book = 0  # 书籍计数器
s = 56  #动态生成url
commitsum = 0

def getHTMLText(url):
    try:
        r = requests.get(url, headers=h)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getHTMLText1(url):
    try:
        r = requests.get(url, headers=h)
        r.raise_for_status()
        r.encoding = r.apparent_encoding  # 注意encoding编码
        return r.content, r.apparent_encoding
    except:
        return ""


def parsePage(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        soup_allli = soup.find_all('li', class_="gl-item")  # 获得所有li标签
        for soup_li in soup_allli:
            global count_book
            count_book = count_book + 1
            print(count_book, file=desf)
            print(count_book)
            soup_name = soup_li.find('div', class_="p-name")  # 获取书名
            print(soup_name.em.get_text())
            print(soup_name.em.get_text(), file=desf)
            soup_price = soup_li.find('div', class_="p-price")  # 获取书的价格
            print(soup_price.i.get_text(), file=desf)
            soup_shop = soup_li.find('div', class_="p-shopnum")  # 获取出版社的名称
            print(soup_shop.a.get_text(), file=desf)
            """# 获取评论数
            soup_comment = soup_li.find('div', attrs={'data-done':'1'})
            print(soup_comment.get_text())  评论数是动态生成的
            """

            # 书的具体细节
            # 获取书的作者姓名
            soup_author = soup_li.find('span', class_="p-bi-name")
            soup_store = soup_li.find('span', class_="p-bi-store")
            soup_date = soup_li.find('span', class_="p-bi-date")
            try:
                print("作者：", soup_author.a.get_text(), file=desf)
            except:
                print("作者：", "作者未知", file=desf)
            try:
                print("书店：", soup_store.a.get_text(), file=desf)
            except:
                print("书店：", "书店未知", file=desf)
            try:
                print("出版日期：", soup_date.a.get_text(), file=desf)
            except:
                print("出版日期：", "出版日期未知", file=desf)

            # 获取书的产品号
            ProductID = soup_li.find('div', class_="p-commit").strong.a['href'].lstrip('https://item.jd.com/').rstrip('.html#comment')
            ProductID = int(ProductID.strip())
            page = random.randint(0, 9)
            try:
                url_json = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=' + str(ProductID) + '&score=0&sortType=5&page=' + str(page) + '&pageSize=10&isShadowSku=0&fold=1'
                comment_json = getHTMLText1(url_json)
                newh = str(comment_json[0], encoding='{}'.format(comment_json[1]))
                num = re.findall(r'\"commentCount\"\:[\d]*', newh)
                num = num[0].split(':')[1]
                print("评论总数", num, file=desf)
            except:
                print("评论总数:", "数目未知", file=desf)
            if count_book > 1500:
                break
    except:
        print("")

def main():
    start_url = 'https://search.jd.com/Search?keyword=python&wq=python&page={}&s='
    html0 = getHTMLText(start_url.format(1) + str(1))
    #parsePage(html0)
    for i in range(52, 54):
        url = start_url.format((2 * i + 3)) + str(56 + i * 60)
        html = getHTMLText(url)
        parsePage(html)


main()




