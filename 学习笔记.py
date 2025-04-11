# Python爬虫（Web Scraping）是指通过编写python程序从互联网上自动抓取信息，并将其存储到本地计算机或数据库中。
# 爬虫的工作原理是模拟浏览器行为，向服务器发送HTTP请求，获取网页内容，然后分析网页内容，提取有效信息，并将其存储到本地。
# 发送HTTP请求：通过HTTP请求从目标网站获取HTML页面，常用的库包括requests。
# 解析HTML内容：获取HTML页面后，需要解析其内容，提取有效信息。常用的库包括BeautifulSoup、lxml、Scrapy。
# 提取数据：通过定位HTML元素（如标签、属性、类名、文本等）来提取数据。
# 存储数据：将提取到的数据存储到本地，如数据库、文件等。


#一.Python requests 模块
# 一个常用的HTTP请求库，可以方便地发送HTTP请求，获取响应内容。

# #导入requests模块
# import requests

# #定义请求的URL
# url = 'https://www.baidu.com'#一个网址的字符串
# #发送GET请求（有两种请求方式：GET和POST）
# response = requests.get(url)
# # 每次调用requests请求之后，会返回一个response对象，包含了服务器返回的响应内容，如状态码、响应头、响应体等。
# print(response.status_code) #打印状态码
# print(response.headers) #打印响应头,字典类型
# print(response.content) #打印响应体（字节流）
# print(response.text) #打印响应体（字符串），unicode类型
# print(response.apparent_encoding) #打印响应体的编码方式
# print(response.url) #打印请求的URL
# print(response.json()) #打印响应体（json格式）

# post()方法可以发送POST请求到指定的url
# requests.post(url,data={key:value},json={key:value}，args)
# url 请求url
# data 发送的数据，字典类型
# json 发送的json数据，字典类型
# args 发送的查询参数，字典类型

# import requests

# url="https://www.runoob.com/"

# #设置请求头，模拟浏览器
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
# }

# kw = {"s":"python 教程"}

# #params参数用于发送请求参数，如查询关键字等
# response = requests.get(url, headers=headers, params=kw)

# print(response.status_code) #打印状态码
# print(response.encoding) #打印响应体的编码方式
# print(response.url) #打印请求的URL
# print(response.text) #打印响应体（字符串）

# resp=requests.post(url,headers=headers,data={"name":"python","age":18})
# print(resp.text) #打印响应体（字符串）

# 二.BeautifulSoup 模块
# 一个用于从网页中提取数据的Python库，特别使用也接卸HTML、XML文档。
# 推荐使用lxml模块，比标准库的HTML解析器速度更快。
# 基本用法：
# 1.通常先用爬虫库如requests获取网页内容，然后用BeautifulSoup解析网页内容，提取数据。

# from bs4 import BeautifulSoup
# import requests

# # 实例1：
# url="https://cn.bing.com/"
# response=requests.get(url)
# response.encoding="utf-8"
"""
使用 requests 库抓取中文网页时，可能会遇到编码问题，导致中文内容无法正确显示，
为了确保能够正确抓取并显示中文网页，通常需要处理网页的字符编码。
自动检测编码 requests 通常会自动根据响应头中的 Content-Type 来推测网页的编码，
但有时可能不准确，此时可以使用 chardet 来自动检测编码。
import chardet
encoding = chardet.detect(response.content)['encoding']
response.encoding = encoding
"""

# if response.status_code==200:
#     # 使用BeautifulSoup解析网页内容
#     soup=BeautifulSoup(response.text,"lxml")

#     title_tag=soup.find("title")
#     if title_tag:
#         print(title_tag.text)
#     else:
#         print("没有找到title标签")
# else:
#     print("请求失败,状态码:",response.status_code)

# 2.查找标签
# BeautifulSoup提供了多种方法来查找网页中的标签，如find()、find_all()、select()等。
# find()方法查找第一个匹配的标签，如果没有找到匹配的标签，则返回None。
# find_all()方法查找所有匹配的标签，返回一个列表。
# select()方法使用CSS选择器查找标签，返回一个列表。

# # 实例2：
# from bs4 import BeautifulSoup
# import requests
# import chardet

# url="https://www.baidu.com/"

# response=requests.get(url)
# encoding=chardet.detect(response.content)['encoding']
# response.encoding=encoding

# soup=BeautifulSoup(response.text,"lxml")

# first_link=soup.find("a")
# print(first_link)
# print("----------------------")

# first_link_url=first_link.get("href")
# print(first_link_url)
# print("----------------------")

# all_links=soup.find_all("a")
# print(all_links)

# 3.获取标签的文本
# 通过get_text()方法可以获取标签的文本内容。

# # 实例3：
# from bs4 import BeautifulSoup
# import requests
# import chardet

# url="https://www.baidu.com/"

# response=requests.get(url)
# encoding=chardet.detect(response.content)['encoding']
# response.encoding=encoding

# soup=BeautifulSoup(response.text,"lxml")

# paragraph_text=soup.find("p").get_text()
# print(paragraph_text)
# print("-------")

# all_text=soup.get_text()
# print(all_text)


# 4.查找子标签和父标签：通过parent和children属性可以查找标签的父标签和子标签。
# 5.查找具有特定属性的标签：
# 查找所有 class="example-class" 的 <div> 标签
# divs_with_class = soup.find_all('div', class_='example-class')

# # 查找具有 id="unique-id" 的 <p> 标签
# unique_paragraph = soup.find('p', id='unique-id')

# 6.高级用法：
