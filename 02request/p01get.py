import requests

r = requests.get("https://www.baidu.com")
print(r.status_code)  # 打印Response对象的状态码，200表示正常，其他表示不正常
print(type(r))
print(r.text)
print(r.encoding)   # 从HTTP header中猜测的响应内容编码方式
print(r.apparent_encoding)  # 从内容中分析出的响应内容编码方式（备选编码方式）
r.encoding = 'utf-8'  # 改变解码方式（response中获取的是二进制数据流，采用不同的解码方式可以得到不同的text），Encoding to decode with when accessing r.text.
print(r.text)
