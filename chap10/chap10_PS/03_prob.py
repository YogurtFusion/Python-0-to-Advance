class Demo:
    a = 4


o = Demo()
print(o.a) #prints the class attributes because the
# instance attributes is not present

o.a = 0 #instance attributes is set

print(o.a) #print the instance attribute because instance attribute is present 

print(Demo.a) #print class attribute