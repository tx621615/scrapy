import re
#重点
# 正则表达式有两种使用方式，一种是通过原生字符串形成的正则表达式规则的函数调用，适合一次性使用
# 还有一种是通过形成正则表达式的对象可以重复使用，有了对象后函数依然是那些方法，但是不用再添加正则表达式了
# match对象
# 最小匹配和贪婪匹配（某个匹配对象中还存在可能匹配的子串）
"""
re.search(pattern, string, flags=0)
∙pattern : 正则表达式的字符串或原生字符串表示
∙string : 待匹配字符串
∙flags : 正则表达式使用时的控制标记
常用标记
re.I re.IGNORECASE 忽略正则表达式的大小写，[A‐Z]能够匹配小写字符
re.M re.MULTILINE 正则表达式中的^操作符能够将给定字符串的每行当作匹配开始
re.S re.DOTALL 正则表达式中的.操作符能够匹配所有字符，默认匹配除换行外的所有字符，加了标记后可以匹配换行符
"""

match = re.search(r"[1-9]\d{5}", "BIT 100081")  #原生字符串，即不把\认为是转义字符
if match:
    print(match.group(0))

# re.match() 从字符串的开始位置起开始匹配
match = re.match(r"[1-9]\d{5}", "BIT 100081")  #字符串开始位置无法匹配为空
if match:
    print(match.group(0))
else:
    print("match为空")

match = re.match(r"[1-9]\d{5}", "100081 BIT")
if match:
    print(match.group(0))

# Re.findall --返回列表类型
ls = re.findall(r"[1-9]\d{5}", "BIT100081 TSU100084")
if ls:
    print(ls)

"""
re.split(pattern, string, maxsplit=0, flags=0)
∙pattern : 正则表达式的字符串或原生字符串表示
∙string : 待匹配字符串
∙maxsplit: 最大分割数，剩余部分作为最后一个元素输出
∙flags : 正则表达式使用时的控制标记
"""

# re.split()
ls1 = re.split(r"[1-9]\d{5}", "BIT100081 TSU100084")
print(ls1) #将匹配的字符串去除，返回被其分割的部分
# 使用maxsplit限制分割的段数
ls1 = re.split(r"[1-9]\d{5}", "BIT100081 TSU100084", maxsplit=1)
print(ls1) #分割成2个，一个为剩余的部分

"""
re.finditer(pattern, string, flags=0)
∙pattern : 正则表达式的字符串或原生字符串表示
∙string : 待匹配字符串
∙flags : 正则表达式使用时的控制标记
搜索字符串，返回一个匹配结果的迭代类型，每个迭代
元素是match对象
"""
for m in re.finditer(r"[1-9]\d{5}", "BIT100081 TSU100084"):
    if m:
        print(m.group(0))    #访问match对象的方法，group(0)表示字符串对象的本身，group(i)表示所采用的re的各个分组

"""
re.sub(pattern, repl, string, count=0, flags=0)
∙pattern : 正则表达式的字符串或原生字符串表示
∙repl : 替换匹配字符串的字符串
∙string : 待匹配字符串
∙count : 匹配的最大替换次数
∙flags : 正则表达式使用时的控制标记
在一个字符串中替换所有匹配正则表达式的子串
返回替换后的字符串
"""

#re.sub(), repl, count两个函数
print(re.sub(r"[1-9]\d{5}", ":zipcode", "BIT100081 TSU100084"))

#通过re.compile()函数形成正则表达式
pat = re.compile(r"[1-9]\d{5}")
print(pat.search("BIT100081 TSU100084").group(0))


# match对象
"""
Match对象是一次匹配的结果，包含匹配的很多信息
属性
.string 待匹配的文本
.re 匹配时使用的patter对象（正则表达式）
.pos 正则表达式搜索文本的开始位置
.endpos 正则表达式搜索文本的结束位置
方法
.group(0) 获得匹配后的字符串   #注意正则表达式是模糊搜索
.start() 匹配字符串在原始字符串的开始位置
.end() 匹配字符串在原始字符串的结束位置
.span() 返回(.start(), .end())
"""
m = re.search(r"[1-9]\d{5}", "BIT100081 TSU100084")
print(m.string)
print(m.re)
print(m.pos)  # search从字符串的开始查找到字符串的末尾
print(m.endpos)
print(m.group(0))  # 注意search只是返回第一个匹配的对象，但是finditer返回所有对象
print(m.start())
print(m.end())
print(m.span())


# 贪婪匹配：Re库默认采用贪婪匹配，即输出匹配最长的子串
match = re.search(r'PY.*N', 'PYANBNCNDN')  # 有多个匹配的结果（注意是同一个字符串中的各个子串）
print(match.group(0))

"""
最小匹配
使用不同的操作符进行匹配：通配符+？，以及表示范围的{}后加？表示最小匹配
*? 前一个字符0次或无限次扩展，最小匹配
+? 前一个字符1次或无限次扩展，最小匹配
?? 前一个字符0次或1次扩展，最小匹配
{m,n}? 扩展前一个字符m至n次（含n），最小匹配
"""