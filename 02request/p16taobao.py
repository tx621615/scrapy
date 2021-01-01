import requests
import re
import bs4
# 目标：获取淘宝搜索页面的信息，提取其中的商品价格和名称
# 理解：淘宝的搜索接口，翻页处理

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding  # 注意encoding编码
        return r.text
    except:
        return ""


def parsePage(ilt, html):   # 注意如果解析可以直接查找，那么就可以不用bs4
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)  #使用rawstring还是要转义
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        print(plt)
        for i in range(len(plt)):  # plt是列表
            price = eval(plt[i].split(':')[1])   # 把字符进行分割，获得值的部分,eval去掉字符串的双引号
            #title = eval(tlt[i].split(':')[1])
            ilt.append(price)
    except:
        print("")



def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"  # 输出信息的格式
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count, g[0], g[1]))



def main():
    goods = '书包'
    depth = 2
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
        printGoodsList(infoList)

main()