def hello():
    print("Hello World")


hello()


def add(n1, n2):
    return n1 + n2


print(add(1, 5))


def result_even(num):
    list = []
    for i in num:
        if i % 2 == 0:
            list.append(i)
    return list


print(result_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))
