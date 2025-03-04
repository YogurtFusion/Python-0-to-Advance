from functools import reduce
a = [111, 3, 65, 54332, 44, 23, 23 ,123, 34]

def greater (a, b):
    if a > b:
        return a
    return b


print(reduce(greater, a))