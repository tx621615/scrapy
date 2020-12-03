# 使用Python获取ip地址归属地
# 实际上是访问别人判断Ip地址归属地的查询的网站
# 人与网站的交互模式，实际上是是以链接形式提交的，只要你知道向后台提交的链接形式，就可以通过Python代码模拟，而不是通过网站交互
# 访问某个链接不一定该链接就对应某个具体文件，可能只是通过该链接向服务器发送数据，然后服务器根据你提供的数据，再返回某个具体文件（或者说数据响应），url当然也可以指某个文件。(因为用户不清楚具体文件路径，因此一般通过url传输数据，服务器根据数据返回对应的文件)
# 必须从爬虫视角看待网络内容，人类通过浏览器访问对应资源，实质上是通过访问对应文件的url来获取该文件，因此只要模拟构造对应的url就可以通过Python爬虫来获取内容。
import requests
url = "https://m.ip138.com/iplookup.asp?ip="
url1 = "https://m.ip138.com/iplookup.asp?"
kv = {'User-Agent': 'Mozilla/5.0'}  # 隐藏python爬取信息，伪装成浏览器查询
try:
    r = requests.get(url + "202.204.80.112", headers=kv)   # 这里也可以加上参数查询，实际上都是访问同一个url
    #r = requests.get(url1, params={"ip": "202.204.80.112"}, headers=kv)
    print(r.request.headers)
    r.raise_for_status()
    r.encoding = 'utf-8'
    print(r.text)
except:
    print("抓取失败")

