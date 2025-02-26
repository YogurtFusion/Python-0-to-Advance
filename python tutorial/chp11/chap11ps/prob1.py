class TwoVector:
    def __init__(self, i ,j):
        self.i = i
        self.j = j
        #print(f"Here i is {self.i}i and j is {self.j}j")

    def show(self):

        print(f"Here i is {self.i}i and j is {self.j}j")


class ThreeVector(TwoVector):
    def __init__(self, i, j, k):
        #here
        super().__init__(i, j)
        self.k = k
   #     print(f"Here i is {self.i}i and j is {self.j}j and {self.k}k ")

    def show(self):
        print(f"here vectors are {self.i}i, {self.j}j and {self.k}k")

# r = TwoVector(23, 3)
# print(r)

# we = ThreeVector(12, 324, 342)
# print(we) 
# commented out parts are the not good way of code because it is nither flexible nor stops Unnecessary prints


a = TwoVector(1, 2)
a.show()

b = ThreeVector(1, 2, 3)
b.show()
