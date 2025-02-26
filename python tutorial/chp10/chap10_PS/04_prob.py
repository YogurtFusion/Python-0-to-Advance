class calculator:
    def __init__(self, n):
        self.n = n
    
    def square(self):
        print(f"Here is your square {self.n * self.n}")

    def cube(self):
        print(f"Here is your cube {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"here is your {self.n**(1/2)}")
    

    @staticmethod
    def hello():
        print("Hey there!!!")

a = calculator(9)

a.square()
a.cube()
a.squareroot()
a.hello()