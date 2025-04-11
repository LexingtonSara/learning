#-*- coding:utf-8 -*-
import requests
import re
import csv

#1.找到电影天堂的搜索页面的url
#2.定位到IMDB评分8分左右影片500余部
#3.从IMDB评分8分左右影片500余部中提取到子页面的链接地址
#4.爬取子页面，提取电影名称、导演、主演、评分、评价人数、评价内容、下载链接
#5.将数据保存到csv文件中

#1.找到电影天堂的搜索页面的url
# base_url="https://dydytt.net/index.htm"

# resp=requests.get(base_url)
# resp.encoding='gb2312'
# print(resp.text)#成功获取源代码

with open('IMBD评分8分左右影片.csv','w',newline='',encoding='utf-8',errors='ignore') as f:
    writer=csv.writer(f)
    writer.writerow(['电影名称','下载链接'])


#2.IMDB评分8分左右影片500余部
url="https://dydytt.net/html/gndy/jddy/20160320/50523.html"
resp=requests.get(url)
resp.encoding='gb2312'
# print(resp.text)#成功获取源代码

obj=re.compile(r'<br /><a href="(?P<url>.*?)">https.*?</a>',re.S)
urls=obj.finditer(resp.text)
for url in urls:
    print(url.group('url'))#提取子页面的链接地址
    #4.爬取子页面，提取电影名称、下载链接
    sub_url=url.group('url')
    sub_resp=requests.get(sub_url)
    sub_resp.encoding='gb2312'
    # print(sub_resp.text)#成功获取源代码

    sub_obj=re.compile(r'◎译　　名(?P<name>.*?)<br />.*?href="(?P<download>.*?)">',re.S)
    result=sub_obj.search(sub_resp.text)
    # print(result.group('name'))
    # print(result.group('download'))#提取电影名称、下载链接
    #5.将数局保存到csv文件中
    with open('IMBD评分8分左右影片.csv','a',newline='',encoding='utf-8',errors='ignore') as f:
        writer=csv.writer(f)
        writer.writerow([result.group('name'),result.group('download')])

    sub_resp.close()
resp.close()

print('爬取完成')

