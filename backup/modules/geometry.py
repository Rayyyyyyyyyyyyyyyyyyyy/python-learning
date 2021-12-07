# 計算兩點的距離
def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


# 計算斜率
def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)
