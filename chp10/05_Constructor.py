class Employee: #class is like empty form 
    #this is class attribute
    language = "Python"
    salary = 1200000

    def __init__(self, name, language, salary):#dunder method which is automatically called 
        self.name = name
        self.language = language
        self.salary = salary
        print("I'm a object")


    def get_info(self):
        print(f"Here is your salary is {self.salary} and your language {self.language}")
    
    @staticmethod
    def greet():
        print("have a good day")         


data = Employee("Aniket", "python", 1300000) #data is object/instance attribute 
print(data.name, data.salary, data.language)
# data.name = "Harry"
# data.get_info()
# print(data.language)
# data.greet()
