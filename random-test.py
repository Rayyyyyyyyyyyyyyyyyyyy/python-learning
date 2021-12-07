# # 亂數
# import random

# data = random.choice([213, 23, 151, 23])
# print(data)  # 隨機選1筆

# data = random.sample([23, 41, 24, 52, 32], 3)
# print(data)  # 隨機選3筆

# data = [3, 24, 1, 52, 2]
# random.shuffle(data)
# print(data)  # 洗牌

# data = random.random()
# print(data)  # 0-1 隨機亂數

# data = random.uniform(60, 100)
# print(data)  # 自訂範圍的隨機亂數

# data = random.normalvariate(100, 10)
# print(data)  # 以第一個參數為基準 大多會顯示 正負 第二個參數

# 統計
import statistics as stat

data = stat.mean([2, 4, 2, 5, 2, 45, 1111])  # 平均
print(data)

data = stat.median([2, 4, 2, 5, 2, 45, 1111])  # 中位數
print(data)

data = stat.stdev([2, 4, 2, 5, 2, 45, 1])  # 標準差 資料散佈的狀況
print(data)
