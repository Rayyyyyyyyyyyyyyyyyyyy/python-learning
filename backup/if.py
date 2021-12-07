# x = input("enter num: ")  # 取得字串形式的使用者輸入
# x = int(x)  # 轉換成數字 str -> int
# if x > 10:
#     print(x, "> 10")
# elif x > 5:
#     print("5 <", x, "< 10")
# else:
#     print(x, "< 5")

n1 = int(input("enter num1: "))
n2 = int(input("enter num2: "))
# print(n1 + n2)
op = input("do what:")
if op == "*":
    print(n1 * n2)
elif op == "+":
    print(n1 + n2)
elif op == "/":
    print(n1 / n2)
elif op == "-":
    print(n1 - n2)
else:
    print("error")
