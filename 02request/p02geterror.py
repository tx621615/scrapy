"""
通用代码框架，使得连接出现异常时能够处理
"""
import requests

# 测试r.raise_for_status()


def getHTML(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


if __name__ == "__main__":
    url = "www.baidu.com"
    print(getHTML(url))
