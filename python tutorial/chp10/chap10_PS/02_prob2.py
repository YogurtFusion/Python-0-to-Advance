class calculator:
    def __init__(self, n):
        self.n = n
    
    def square(self):
        print(f"Here is your square {self.n * self.n}")

    def cube(self):
        print(f"Here is your cube {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"here is your {self.n**(1/2)}")


a = calculator(9)

a.square()
a.cube()
a.squareroot()

# * is for multiply and ** is for power
# code by gpt

import math  # For square root calculation

class Calculator:
    def find_square(self, num):
        return num ** 2          # Square = number raised to the power of 2

    def find_cube(self, num):
        return num ** 3          # Cube = number raised to the power of 3

    def find_square_root(self, num):
        return math.sqrt(num)    # Using math module to find square root
        # OR you can simply use: return num ** 0.5

# Creating an object of the Calculator class
calc = Calculator()

# Example usage
number = 16
print(f"Square of {number}: {calc.find_square(number)}")
print(f"Cube of {number}: {calc.find_cube(number)}")
print(f"Square Root of {number}: {calc.find_square_root(number)}")
