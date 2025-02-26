import random

def game():
    print("you are playing the game")
    score = random.randint(1, 62)
    #score2 = random.randint(1, 62)
    #fetc the highscore
    with open("highscore.txt", "r") as f:
        highscore = f.read()
        if (highscore!=""):
            highscore = int(highscore)
        else:
            highscore = 0
    
    print(f"your score: {score}")
    if(score>highscore):
        with open("highscore.txt", "w") as f:
          f.write(str(score))
        # with open("highscore.txt", "a") as r:
        #     r.write(str(score2))  
    return score


#Quest for me let's create a highscore history

    

game()
