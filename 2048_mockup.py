import random

print ('==============================================')
print ('Simple mockup of 2048 game, made by Heejong Ahn')
print ('You can see the code in github.com/heejongahn')
print ('==============================================')
print ('\n')

n = input('Size of the table? ')


def makeTable(n):
    table = [0] * n
    for i in range(n):
        table[i] = ['-'] * n
    table[0][0] = 2
    return table

def printTable(table):
    for line in table:
        for e in line:
            print (e),
        print ('\n')
    return

def pickGrid(table, freeList):
    grid = random.choice(freeList)
    table[grid//4][grid%4] = 2
    return

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

def moveUp():
    global table

    for col in range(0, 4):
        for i in range(0, 3):
            for j in range(i+1, 4):
                if table[i][col]!= '-' and table[i][col] == table[j][col]:
                    table[j][col] = '-'
                    table[i][col] = table[i][col] * 2
                    break

        for i in range(0, 3):
            for j in range(i+1, 4):
                if table[i][col]== '-' and table[j][col]!= '-':
                    table[i][col] = table[j][col]
                    table[j][col] = '-'
                    break

table = makeTable(n)
printTable(table)


while (freeList!= []):
    while True:
        usrInput = input("Pick a move : up/down/left/right ")
        if not makeMove(usrInput):
            break

    pickGrid
