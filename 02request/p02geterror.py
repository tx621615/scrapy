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


if __name__ == "__main__":     # 如果模块是直接运行则运行，如果模块是被导入的则不运行代码，python没有main函数入口，那么只能一句句解释，所以import的模块也可能运行
    url = "www.baidu.com"
    print(getHTML(url))

