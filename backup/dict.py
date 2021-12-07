# # 集合
# s1 = {3, 4, 5, 6}
# # 有沒有在裡面
# print(3 in s1)
# print(10 not in s1)

# s2 = {3, 5, 6, 7, 8, 9, 1, 23, 5, 6, 7, 34, 1}
# s3 = s1 & s2  # 交集 取兩個都有
# print("交集:", s3)

# s4 = s1 | s2  # 聯集 合併但若重複就只取一個
# print("聯集:", s4)

# s5 = s2 - s1  # 差集 減去重疊
# print("差集:", s5)

# s6 = s1 ^ s2  # 反交集 取兩個不重疊
# print("反交集:", s6)

# s = set("Hello")  #set(字串) 拆解成集合 過濾重複
# print(s)

# 字典 { key: value }
# dic = {"a": "apple", "b": "bug"}
# # dic["a"] = "big apple"
# # print(dic)
# del dic["a"]  # 刪除指定組
# print(dic)

dic = {x: x * 2 for x in [3, 5, 67, 2]}  # 使用列表資料產生字典
print(dic)
