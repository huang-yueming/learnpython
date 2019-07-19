#正则表达式知识
#re.match
#学习连接  https://www.runoob.com/python/python-reg-expressions.html
#re.match  re.search 搜索  re.sub 检索与替换  re.compile 编译正则表达式 
#findall 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表
#re.finditer在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
#split 方法按照能够匹配的子串将字符串分割后返回列表
import re
#读取文件
f = open(r"C:\Users\黄铭政\Desktop\信号强度.txt",'r')
line=f.read()
f.close()
pattern=re.compile(r'\-\d{2}')  #正则表达式公式
result=pattern.findall(line)
print(result)
num=''.join(result)
f=open(r"C:\Users\黄铭政\Desktop\信号强度修改.txt",'w')   #r一定要加  否则会造成编码错误
f.write(num)
f.close()


