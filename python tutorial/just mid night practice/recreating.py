import random

n = random.randint(1, 100)
a = -1
guess = 0

while a != n:
    guess +=1
    a = (int(input("Enter your no: ")))
    if a>n:
        print ("select some lower no.")

    elif a<n:
        print("select some higher no.")

print("you guessed right ")
    
