'''
sum(1) = 1  
sum(2) = 1 + 2  
sum(3) = 1 + 2 + 3 
sum(4) = 1 + 2 + 3 + 4 
sum(5) = 1 + 2 + 3 + 4 + 5 

sum(n) = 1 + 2 + 3 + 4 + 5..... n-1 + n  
sum(n) = sum(n-1) + n 
'''

def sum(n):
    if(n==1):
        return 1
        #what if return would be there???
    return sum(n-1) + n

print(sum(int(input("enter your no: "))))


# Here n-1 works till is does not come to 1. but why it stops a at 1 (maybe due to return) and then it adds all the values 