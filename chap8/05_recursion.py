'''
Factorial(0) = 0
Factorial(1) = 1
Factorial(2) = 2 X 1
Factorial(3) = 3 X 2 X 1
Factorial(4) = 4 X 3 X 2 X 1
Factorial(5) = 5 X 4 X 3 X 2 X 1
Factorial(n) = n X n-1 X.......3 X 2 X 1

Factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if(n==1) or (n==0): #what is the fucn of and 
        return 1
    return n * factorial(n-1) # how python knows that it wants to process n-1 first then n* n-1 

n = int(input("Enter your number: "))
print(f"The factorial of the given no. is: {factorial(n)} ")