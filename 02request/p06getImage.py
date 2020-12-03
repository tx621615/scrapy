# 从网络上获取一个图片（一般以jpg格式结尾），图片实际内容为2进制
import requests
import os
url = "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1849459778,3492875633&fm=26&gp=0.jpg"  # 点击图片右键赋值Url即可
# 设置获取文件后存储在本机哪个位置,注意windows下文件采用反斜杠\来表示路径，但是在字符串中反斜杠用做转义字符因此使用双反斜杠\\
path = "C:\\Users\\71058\\Desktop\\epub\\a.jpg"
r = requests.get(url)
print(r.status_code)  # 200获取成功
# print(len(r.text))   # 图片采用字符串解释出现乱码
# print(r.text[:100])
# 已经获得了这个文件那么接下来就是如何将其内容保存在本地电脑中，我们采用文件写方法将内容写入即可

with open(path, "wb") as f:
    f.write(r.content)  # 如果路径中没有文件则创建一个空文件，通过content获得返回的二进制形式的内容，note:每次写都是从头开始写，因此永远可以写，哪怕文件存在

f.close()


# 更加优化（排除错误）的写法
url = "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1849459778,3492875633&fm=26&gp=0.jpg"
root = "C:\\Users\\71058\\Desktop\\epub"   # 为了能够灵活的命名文件，可以使用网站上的名字也可以使用自己定义的名字
path = root + "\\安达与岛村.jpg"
try:
    if not os.path.exists(root):  # 判断根目录是否存在
        os.mkdir(root)
    if not os.path.exists(path):  # 判断文件是否已经存在
        r = requests.get(url)
        r.raise_for_status()
        with open(path, "wb") as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已经存在")
except:
    print("爬取失败")