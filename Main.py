# 2048 Mockup in Python3 : Made by Heejong Ahn

from Table import Table
from Score import Score
import Getch
import os
import platform

isWindows = True if platform.system() == 'Windows' else False

#### Main routine

os.system('cls' if isWindows else 'clear')

# Make a Score instance
score = Score()
bestScores = score.bestScores

# Try to make a Table instance
try:
    table = Table()

# If user types any non-integer value at the first place, print the
# scoreboard and end the program.
except:
    score.printScoreboard()
    input("Insert any key to quit... ")

# Elsewhere, the game starts
else:
    try:
        table.setBestScore(int(bestScores[0][0]))
    except:
        table.setBestScore(0)

    while (table.canMove()):
        # Use Getch module to handle inputs without entering
        usrInput = Getch.getch()

        # User can quit the game anytime by typing 'q'
        if usrInput == 'q':
            break

        # Handles invalid inputs
        if table.makeMove(usrInput):
            continue

        # When table is full and a move toward invalid direction is made, ignore it.
        try:
            table.pickGrid()
        except:
            pass

        # Clear the terminal everytime
        os.system('cls' if isWindows else 'clear')
        table.printTable()

        # When the goal is achieved
        if table.isGoal():
            print ("You won !!! Your final score is: ", end =" ")
            print (table.getScore())
            while True:
                name = input ("Type your name to quit. (4~10 words) ")
                if len(name)<4 or len(name)>10:
                    print ("Please type a valid name.")
                    continue
                break

            score.updateScoreboard([table.getScore(), name])

    # When There's no possibly way to win
    print ("You lost... Your final score is: ", end =" ")
    print (table.getScore())
    while True:
        name = input ("Type your name to quit. (4~10 words) ")
        if len(name)<4 or len(name)>10:
            print ("Please type a valid name.")
            continue
        break

    score.updateScoreboard([table.getScore(), name])
