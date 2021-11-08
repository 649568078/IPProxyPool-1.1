import requests
from lxml import etree


url = "https://www.w3school.com.cn/xpath/xpath_axes.asp"
res = requests.get(url).text
html = etree.HTML(res)
a = html.xpath("(//table[@class='dataintable'])[1]/tr")
print(a)

for i in a:
    s = i.xpath(".//td")
    print(s)
    print(len(s))
