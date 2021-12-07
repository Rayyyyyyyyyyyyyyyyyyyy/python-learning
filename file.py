# # 寫入檔案 就算不存在也會自動建立

# # file = open("data.txt", mode="w", encoding="utf-8")  # 開啟檔案
# # file.write("你好 file\nno2")  # 操作
# # file.close()  # 關閉

# with open("data.txt", mode="w", encoding="utf-8") as file:
#     file.write("3\n14\n200")

# # 讀取現有的檔案
# # 把檔案的資料一行一行的讀取
# sum = 0
# with open("data.txt", mode="r", encoding="utf-8") as file:
#     # data = file.read()
#     for line in file:
#         sum += int(line)
# print(sum)

# 使用 ＪＳＯＮ 格式讀取,複寫
import json
with open("config.json", mode="r") as file:
    data = json.load(file)
print(data)  # 字典資料
# 讀取 json 放入變數
data["name"] = "new name"
with open("config.json", mode="w") as file:
    json.dump(data, file)
# 將更新的資料放回 json
print(data)
