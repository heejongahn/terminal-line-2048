from Table import Table
import Getch

# 2048 Mockup in Python3 : Made by Heejong Ahn

# Main routine

table = Table()

while (table.canMove()):
    print("Pick a move : w(up) / s(down) / a(left) / d(right) or q(quit)")
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

    table.printTable()
    # When the goal is achieved
    if table.isGoal():
        print ("You won !!! Your final score is: ", end =" ")
        print (table.point)
        input ("Insert any key to quit... ")

# When There's no possibly way to win
print ("You lost... Your final score is: ", end =" ")
print (table.point)
input ("Insert any key to quit... ")

