#5! = 1 X 2 X 3 X 4 X 5

n = int(input("Enter your number: "))
 
product = 1 
#In addition we use 0 to inciate but in multiplications we use 1

for i in range(1, n+1):
    product = product * i

print(f"The factorial of {n} is {product}")
