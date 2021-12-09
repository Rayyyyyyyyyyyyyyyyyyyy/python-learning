import urllib.request as req
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.ptt.cc/bbs/Japandrama/index.html"
request = req.Request(
    url,
    headers={
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    })

with req.urlopen(request) as res:
    data = res.read().decode("utf-8")
# print(data)

import bs4

root = bs4.BeautifulSoup(data, "html.parser")  # BeautifulSoup 套件使用 解析 html
# print(root.title.string)
titles = root.find_all("div", class_="title")  # 尋找所有 class= "title" 的 div
# print(titles)
for title in titles:
    if title.a != None:
        print(title.a.string)