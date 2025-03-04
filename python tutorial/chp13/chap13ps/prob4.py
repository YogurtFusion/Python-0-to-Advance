def divisible5(n):
    if n%5 ==0:

        return True
    return False


a = [42, 234245, 15123440, 43523, 51353, 1545, 12344]

f = list(filter(divisible5, a))

print(f)