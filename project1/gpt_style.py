import random

'''
1 is for snake
-1 is for water
0 is for gun 
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s for Snake, g for Gun, w for Water): ").lower()  # Handling lowercase input
youdict = {"s": 1, "g": 0, "w": -1}  # Corrected to lowercase 'w'
reverseDict = {1: "Snake", 0: "Gun", -1: "Water"}

# Validate user input
if youstr not in youdict:
    print("Invalid input! Please choose 's', 'g', or 'w'.")
    exit()

you = youdict[youstr]

# Display choices
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

# Logic to determine the winner
if computer == you:
    print("It's a draw!")

elif (computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1):
    print("You lose!!!")

else:
    print("You win!!!")







#gpt improved shortend code

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

# Determine winner
if computer == you:
    print("It's a draw")
else:
    if (computer - you) == -1 or (computer - you) == 2:
        print("You lose!!!")
    else:
        print("You win!!!")
