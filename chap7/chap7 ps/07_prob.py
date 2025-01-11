'''
  *
 ***
***** for n = 3

'''

n = int(input("Enter your number: "))
for i in range(1, n+1):
    print(""* (n-i), end="")
    print("*"* (2*i-1), end="")
    print("")

    # What is need of n-1 in line 10 i thought py always process n-1
    