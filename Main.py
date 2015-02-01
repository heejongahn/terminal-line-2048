# 2048 Mockup in Python3 : Made by Heejong Ahn

from Table import Table
from Score import Score
import Getch
import os
import platform

isWindows = True if platform.system() == 'Windows' else False

# Main routine

os.system('cls' if isWindows else 'clear')
table = Table()
score = Score()
bestScores = score.loadScoreboard()

try:
    table.setBestScore(int(bestScores[0][0]))
except:
    table.setBestScore(0)

while (table.canMove()):
    usrInput = Getch.getch()
    if usrInput == 'q':
        break
    # Handles invalid inputs
    if table.makeMove(usrInput):
        continue

    # When table is full and make a move toward invalid direction, ignore it.
    try:
        table.pickGrid()
    except:
        pass

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
