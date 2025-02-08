class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"class attribute of a i {cls.a}")




e = Employee()
e.a = 34

e.show()