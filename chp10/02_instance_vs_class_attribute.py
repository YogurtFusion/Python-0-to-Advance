class Employee: #class is like empty form 
    #this is class attribute
    language = "Python"
    salary = 1200000


data = Employee() #data is object/instance attribute 
data.name = "Harry"
data.language = "javascript"
print(data.name, data.salary, data.language)
# print(data.language)
 
data1 = Employee()
data1.name = "Rohan"
data1.language = "c++"
print(data1.name, data1.salary, data1.language)

#instance attributes got prefrence then class
