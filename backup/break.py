# n1 = 0
# n2 = 0
# while n1 < 10:
#     if n1 == 5:
#         break
#     n1 += 1
#     print(n1)

# n = 0
# for x in [0, 1, 2, 3, 4, 5, 6]:
#     if x % 2 == 0:
#         continue
#     n += 1
#     print(n)

# n = 0
# while n < 5:
#     if n == 3:
#         break
#     print(n)
#     n += 1

# print("外面的:", n)

# n = 0
# for x in [0, 1, 2, 3, 4, 5, 6]:
#     if x % 2 == 0:
#         continue  # 符合條件的就跳過
#     print(x)
#     n += 1
# print("外面的n:", n)

# sum = 0
# for n in range(11):
#     sum += n
# else:
#     print(sum)

x = int(input("enter num: "))

for i in range(x):
    if i * i == x:
        print("平方根: ", i)
        break
else:
    print("error")