class micro():
    company = "Microsoft"
    
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
    




d = micro("Rohan", 1200000, 23232)

print(d.name, d.salary, d.pin, d.company)
 
H = micro("Harry", 1300000, 31223) 
print(H.name, H.salary, H.pin, H.company)

