import random

# 2048 Mockup in Python3 : Made by Heejong Ahn


# function initializeGame
# Literally initializes the game: Make a game table and print it

def initializeGame():
    global table
    global n

    print ('==============================================')
    print ('Simple mockup of 2048 game, made by Heejong Ahn')
    print ('You can see the full code in github.com/heejongahn')
    print ('==============================================')
    print ('\n')

    n = int(input('Size of the table? '))
    table = makeTable(n)

    printTable(table)

# function makeTable
# Makes a n*n size game table

def makeTable(n):
    table = [0] * n
    for i in range(n):
        table[i] = ['-'] * n
    table[0][0] = 2
    return table

# function printTable
# Prints current game table state

def printTable(table):
    for line in table:
        for e in line:
            print (e),
        print ('\n')
    return

# function pickGrid
# Pick a free grid from a table and place [2] tile

def pickGrid(table, freeList):
    global n

    grid = random.choice(freeList)
    table[grid//n][grid%n] = 2
    return

# function makeMove
# This is what 2048 is about!

def makeMove(usrInput):
    if usrInput == 'up':
        moveUp()
    elif usrInput == 'down':
        moveDown()
    elif usrInput == 'left':
        moveLeft()
    elif usrInput == 'right':
        moveRight()
    else:
        print ('Please select a valid move')
        return 1
    return 0

# funciton moveUp
# Like other three move functions below,
# 1) Handles the merge first and then
# 2) Handles the blanks

def moveUp():
    global table
    global n

    for col in range(0, n):
        for i in range(0, n-1):
            for j in range(i+1, n):
                if table[i][col]!= '-' and table[i][col] == table[j][col]:
                    table[j][col] = '-'
                    table[i][col] = table[i][col] * 2
                    break

        for i in range(0, n-1):
            for j in range(i+1, n):
                if table[i][col]== '-' and table[j][col]!= '-':
                    table[i][col] = table[j][col]
                    table[j][col] = '-'
                    break


# Main routine

while (freeList!= []):
    usrInput = input("Pick a move : up/down/left/right ")
    if makeMove(usrInput):
        continue
    pickGrid()
    printTable()
