import random
n = random.randint(1, 100)

a = -1

guesses = 0
 

while(a != n):
    guesses +=1
    a = int(input("Guess the no: "))

    if a>n:
        print("please guess lower no.")

    elif(a<n):
        print("print guess higher no:")

    guesses +=1

print(f"you've gueesed the correct no. {n} in total {guesses} attempts  ")