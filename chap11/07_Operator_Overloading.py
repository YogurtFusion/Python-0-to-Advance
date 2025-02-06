class Number:
    def __init__(self, n):
        self.n  = n

        
    def __add__(self, num):
        return self.n + num.n
    

n = Number(1)
m = Number(2)


print(n+m)

'''
p1+p2 # p1.__add__(p2)
p1-p2 # p1.__sub__(p2)
p1*p2 # p1.__mul__(p2)
p1/p2 # p1.__truediv__(p2)
p1//p2 # p1.__floordiv__(p2)
'''