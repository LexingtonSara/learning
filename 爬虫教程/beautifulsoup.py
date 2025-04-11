from bs4 import BeautifulSoup
import requests

url="https://www.4kdesk.com/4kfengjing/"

resp=requests.get(url)
resp.encoding='utf-8'
# print(resp.text)
main_page=BeautifulSoup(resp.text,'html.parser')
alist=main_page.find("div",class_="mt15 clearfix pic-auto pic-list").find_all("a")
for a in alist:
    # print(a.get("href"))
    href=a.get("href")

    detail_page=requests.get(href)
    detail_page.encoding='utf-8'

    detail_soup=BeautifulSoup(detail_page.text,'html.parser')
    