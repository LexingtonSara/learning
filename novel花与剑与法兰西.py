#-*- coding:utf-8 -*-

import requests
from lxml import etree
import time

base_url="https://www.dingdian-xiaoshuo.com/n/huayujianyufalanxi/2675.html"

headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    }
chapter_number=0
for chapter_num in range(2675,3738):
    url=f"https://www.dingdian-xiaoshuo.com/n/huayujianyufalanxi/{chapter_num}.html"
    #1.首先找到目标网址
    # url="https://www.dingdian-xiaoshuo.com/n/huayujianyufalanxi/2675.html"
    
    #2.发送请求获取网页内容
    resp=requests.get(url,headers=headers)
    resp.encoding='utf-8'
    # print(resp.status_code)
    # print(resp.encoding)
    #3.提取目标数据
    # print(resp.text)
    tree=etree.HTML(resp.text)

    content_div=tree.find(".//div[@id='content']")

    if content_div is not None:
        text=content_div.xpath(".//p/text()")
        # print(text)
        with open("花与剑与法兰西.txt","a+",encoding='utf-8') as f:
            f.write("\n".join(text))
            f.write("\n\n")
        chapter_number+=1
        print(f"chaper{chapter_number}Save successfully")

    else:
        print("No content found")

    resp.close()
    time.sleep(1)

