'''
The game() function in a program lets a user play a game and returns the score as an
integer. You need to read a file "Hi-score.txt" which is either blank or contains the previous
Hi-score. You need to write a program to update the Hi-score whenever the game()
function breaks the Hi-score.
'''
import random
def game():
    print("You are playing the game...")
    score=random.randint(1,62)

    #Fetch the High Score
    with open("Hi_score.txt") as f:
        hiscore=f.read()    #By default read show Str values 
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0

    print(f"Your score is {score}")
    if (score>hiscore):

        #Write this hiscore in file
        with open("Hi_score.txt","w") as f:
            f.write(str(score))      # 'Write' expect a score in string so we convert it

    return score

game()

