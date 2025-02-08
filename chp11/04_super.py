class Employee:
    def __init__(self):

        print("constructor of the employee")
    a = 1
class Programmer(Employee):
    def __init__(self):

        print("constructor of the programer")
              
    b = 2

class Manager(Programmer):
   
    def __init__(self):
        super(). __init__()
        print("constructor of the Managaer")

        
    c = Employee.a + Programmer.b



o = Employee()
print(o.a)


p = Programmer()
print(p.a, p.b)


x = Manager()
print(x.a, x.b, x.c)










# Method of calling both Employee AND programmer constructor 

class Employee:
    def __init__(self):

        print("constructor of the employee")
    a = 1
class Programmer(Employee):
    def __init__(self):
        super(). __init__()

        print("constructor of the programer")
              
    b = 2

class Manager(Programmer):
   
    def __init__(self):
        super(). __init__()
        print("constructor of the Managaer")

        
    c = Employee.a + Programmer.b



o = Employee()
print(o.a)


p = Programmer()
print(p.a, p.b)


x = Manager()
print(x.a, x.b, x.c)


