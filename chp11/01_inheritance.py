class Employee:
    company = "ITC"
    def show(self):
        print(f"The nanme of the employee is {self.name} and the salary of the employee is {self.salary}")



# class Programmer:
#     company = "ITC INFOTECH"
#     def show(self):
#         print(f"the name of the employee is {self.name} and the salary of the employee is {self.salary}")
    
#     def showlanguage(self):
#         print(f"THE name is {self.name}and he is good with {self.language} language")

class Programmer(Employee):
    company = "ITC Infotech"
    def language(self):
        print(f"Name of the employee is {self.name} salary of the employee is {self.salary} language that employee prefers is {self.language}")
a = Employee()
b = Programmer()

print(a.company, b.company)