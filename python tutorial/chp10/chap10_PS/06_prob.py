from random import randint

class Train:
    
    def __init__(slf, trainNo):
        slf.trainNo = trainNo #it will work if you write slf instead of self but it is not reccomandable and not a good practice.. 


    def book(self, fro, to):
        print(f"your ticket is book {fro} to {to}.")

    def getstatus(self):
        print(f"train no{self.trainNo} is running on time....")

    def getfare(self, fro, to):
        print(f"ticket no from {fro} to {to} is {randint(2323, 4444)}")



d = Train(23322)

d.book("rampur", "Delhi")

d.getstatus()

d.getfare("rampur", "Delhi")
