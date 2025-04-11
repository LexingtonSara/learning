# #三种数据解析方式：re解析、bs4解析、xpath解析

# 正则表达式:regular expression
# 元字符:具有固定含义的特殊符号
# .:匹配任意字符(除了换行符\n)
# \d:匹配任意数字
# \D:匹配任意非数字
# \s:匹配任意空白字符(包括空格、制表符、换行符)
# \S:匹配任意非空白字符
# \w:匹配任意字母、数字或下划线
# \W:匹配任意非字母、数字或下划线
# []:匹配括号内的任意字符
# [^]:匹配不在括号内的任意字符
# *:匹配前面的字符0次或多次
# +:匹配前面的字符1次或多次
# ?:匹配前面的字符0次或1次
# {n}:匹配前面的字符恰好n次
# {n,m}:匹配前面的字符n到m次
# ^:匹配字符串的开头
# $:匹配字符串的末尾
# \b:匹配单词的边界
# \B:匹配非单词边界
# \n、\t、\r:匹配换行符、制表符、回车符
# .*:贪婪匹配
# *?、+?、??、{n,m}?、{n,}?:非贪婪匹配/惰性匹配
# \A、\Z:匹配字符串的开头或末尾

# re模块:
# re.findall(pattern, string, flags=0):在string中找到所有匹配正则表达式pattern的子串,并返回一个列表
# re.finditer(pattern, string, flags=0):在string中找到所有匹配正则表达式pattern的子串,并返回一个迭代器
# 从迭代器中拿到内容使用.group()方法
# re.search(pattern, string, flags=0):在string中搜索正则表达式pattern的第一次出现,并返回一个Match对象
# re.match(pattern, string, flags=0):从字符串开头匹配正则表达式pattern,并返回一个Match对象

# 预加载正则表达式:obj=re.compile(pattern, flags=0)


#1.拿到页面源代码
#2.通过re模块获取信息

import requests
import re
import csv

base_url="https://movie.douban.com/top250"

headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

with open("douban_top250.csv","w",newline="",encoding="utf-8-sig") as f:
    writer=csv.writer(f)
    writer.writerow(["电影名","年份","评分","评价人数"])

page=1
while page<=10:
    url=base_url+"?start={}&filter=".format(str((page-1)*25))
    page+=1
    resp=requests.get(url,headers=headers)
    # print(resp.text)#能看到页面源代码
    page_content=resp.text

    #3.解析页面源代码
    obj=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                r'</span>.*?<p>.*?<br>(?P<year>.*?)'
                r'&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)'
                r'</span>.*?<span>(?P<people>.*?)人评价</span>',re.S)

    #开始匹配
    result=obj.finditer(page_content)

    #4.保存数据
    with open("douban_top250.csv","a",newline="",encoding="utf-8-sig") as f:
        writer=csv.writer(f)
        for it in result:
            writer.writerow([it.group("name"),it.group("year").strip(),it.group("score"),it.group("people")])

print("保存成功")
