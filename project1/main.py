import random
'''
1 is for snake
-1 is for water
0 is for gun 
'''
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ").lower()
youdict = {"s": 1, "g": 0, "w": -1}
reverseDict = {1: "Snake", 0: "Water", -1: "Gun"}

# Validate user input
if youstr not in youdict:
    print("Invalid input! Please choose 's', 'g', or 'w'.")
    exit()

you = youdict[youstr]

# by now we've two variables you and computer
print(f"you choose {reverseDict[you]}\ncomputer choose {reverseDict[computer]}")

if (computer == you):
    print("its a draw")

else:
    if((computer - you) == -1 or (computer - you) == 2 ):
        print("you lose!!!")
    else:
        print("you win!!!")



    # if(computer == -1 and you == 1):
    #     print("you won!!!")
    
    # elif(computer ==-1 and you == 0):
    #     print("you loose!!!")
    
    # elif(computer == 1 and you == -1):
    #     print("you loose!!!")
    
    # elif(computer == 1 and you == 0):
    #     print("you win!!!")
    
    # elif(computer == 0 and you == -1):
    #     print("you won!!!")
    
    # elif(computer == 0 and you == 1):
    #     print("you loose!!!")
    
    # else:
    #     print("something error")

        