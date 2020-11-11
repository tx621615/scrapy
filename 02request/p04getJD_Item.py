"""
利用Requests库获取京东某个页面
"""
import requests


def getItem(url):
    try:

        kv = {'User-Agent': 'Mozilla/5.0'}

        # r = requests.get(url)
        # 通过resquests中Request对象来发送http的请求报文，回复报文由Respones对象来接收，但Response对象不仅仅包含这些内容
        r = requests.get(url, headers=kv)  # 采用headers参数对头部请求的头部进行修改，将user-agent字段改为浏览器Mozilla/5.0,而不是python-requests库，JD会根据该字段屏蔽一些爬虫
        r.raise_for_status()
        print(r.request.headers)   # response对象也包含了请求的相关内容
        print(r.encoding)
        r.encoding = r.apparent_encoding
        print(r.encoding)
        print(r.request.headers)
        print(r.text)

    except:
        print("爬取失败")


if __name__ == "__main__":
    url = "https://item.jd.com/10023620229651.html"
    getItem(url)
