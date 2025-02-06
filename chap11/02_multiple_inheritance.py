class Employee:
    company = "ITC"
    name = "charlie"
    salary = 1299999
    def show(self):
        print(f"The nanme of the employee is {self.name} and the salary of the employee is {self.salary}")



class coder:
    language = "python"

    def lang(self):
        print(f"our new coder love {self.language}")


class Programmer(Employee, coder):
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"Name of the employee is {self.name} salary of the employee is {self.salary} language that employee prefers is {self.language}")
a = Employee()
b = Programmer()

#b.show()
b.showlanguage()
#b.lang()