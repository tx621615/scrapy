# 根据关键词获得百度返回页面
# 关键在于模仿平常搜索中关键词进行后的url
# 因此只需要向url中添加数据即可(?后面添加数据)
# http://www.baidu.com/s?wd=keyword(百度关键词对应的HTML页面)

import requests

keyword = "Python"
try:
    kv = {'wd': keyword}
    r = requests.get("http://www.baidu.com/s?", params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))

except:
    print("爬取失败")