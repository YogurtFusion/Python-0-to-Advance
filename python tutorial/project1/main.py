import random

'''
1 is for snake
-1 is for water
0 is for gun 
'''

# Generate computer's choice
computer = random.choice([-1, 0, 1])

# Get user input
youstr = input("Enter your choice (s for Snake, g for Gun, w for Water): ").lower()
youdict = {"s": 1, "g": 0, "w": -1}
reverseDict = {1: "Snake", 0: "Gun", -1: "Water"}

# Validate user input
if youstr not in youdict:
    print("Invalid input! Please choose 's', 'g', or 'w'.")
    exit()

you = youdict[youstr]

# Display choices
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# Check result
if computer == you:
    print("It's a draw!")
else:
    if computer == -1 and you == 1:
        print("You won!!!")
    elif computer == -1 and you == 0:
        print("You lose!!!")
    elif computer == 1 and you == -1:
        print("You lose!!!")
    elif computer == 1 and you == 0:
        print("You win!!!")
    elif computer == 0 and you == -1:
        print("You won!!!")
    elif computer == 0 and you == 1:
        print("You lose!!!")
    else:
        print("Something went wrong!")

        print("something error")

        