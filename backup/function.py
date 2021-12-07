# def get_num(x):
#     print(x)

# get_num(10)

# def multiply(n1, n2):
#     # print(n1 * n2)
#     return n1 * n2 + n1

# mm = multiply(3, 6)
# print(mm)


def avg(*ns):
    sum = 0
    for n in ns:
        sum = sum + n

    print(sum / len(ns))


avg(3, 4)
avg(3, 5, 10)
avg(4, -6)
