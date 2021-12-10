import urllib.request as request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# src = "https://www.ntu.edu.tw/"

# with request.urlopen(src) as response:
#     data = response.read().decode("utf-8")  # 取得網頁原始碼
# print(data)

import json

src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data = json.load(response)  # 利用 json 模組 解析 json 檔案
# print(data)

# 取出公司名稱

clist = data["result"]["results"]
# print(clist)

with open("data.txt", "w", encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"] + "\n")
