class Employee: #class is like empty form 
    #this is class attribute
    language = "Python"
    salary = 1200000

    def get_info(self):
        print(f"Here is your salary is {self.salary} and your language {self.language}")

    def greet(self):
        print("have a good day")         


data = Employee() #data is object/instance attribute 
data.name = "Harry"
print(data.name, data.salary, data.language)
data.get_info()
# print(data.language)
data.greet()
