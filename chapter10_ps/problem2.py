
import random

def game():
    welcome =  "Welcome to the Game!"
    center = welcome.center(50,"-")
    print("\n",center,"\n")
    print("I'm thinking of a number between 1 and 100.")
    print("lates check whose number is highest.. ?")
    score = random.randint(1,100)
    with open("game.txt") as f:
        hiscore = f.read();
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"High Score: {hiscore}")
    print(f"your Score: {score}")

    if(score > hiscore):
       with open("game.txt", "w") as f:
           f.write(str(score))
    return score


game()


