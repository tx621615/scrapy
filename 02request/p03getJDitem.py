"""
利用Requests库获取淘宝某个页面
"""
import requests


def getItem(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.encoding)
        print(r.text)
    except:
        print("爬取失败")


if __name__ == "__main__":
    url = "https://detail.tmall.com/item.htm?spm=a230r.1.14.22.32f93a463nkQQ6&id=628406811872&ns=1&abbucket=1"
    getItem(url)
