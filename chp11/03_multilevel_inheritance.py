class Employee:
    a = 1
class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = Employee.a + Programmer.b



o = Employee()
print(o.a) #print the attribute 4
#print(o.b)#shows an error as there is no b arrtibute in Employee class


p = Programmer()
print(p.a, p.b)


x = Manager()
print(x.a, x.b, x.c)