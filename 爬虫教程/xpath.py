import requests
from lxml import etree
url="https://www.zbj.com/fw/?k=saas"

resp=requests.get(url)

# print(resp.text)
html=etree.HTML(resp.text)

divs=html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div')

for div in divs:
    price=div.xpath("./div/div[3]/div[1]/span[1]/text()")[0].strip("¥")
    title="saas".join(div.xpath("./div/div[3]/div[2]/a[1]/span[1]/text()"))
    # company_address=div.xpath("./div/div[4]/div/text()")#隐藏的标签内容，无法获取
    company_name=div.xpath("./div/div[5]/div[1]/div[1]/div[1]/text()")[0]
    print(company_name)
    print(title)
    print(price)
    

resp.close()
