a = int(input("Enter your no: "))
b = int(input("Enter your no: "))

if(b == 0):

    raise ZeroDivisionError("Heyy our program is not meant to be devide no. by zero")
 
else:
    print(f"the devision a/b is {a/b}")