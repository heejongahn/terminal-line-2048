import random

# 2048 Mockup in Python3 : Made by Heejong Ahn


class Table():


    # function __init__
    # Initializes the game: Make a game table and print it

    def __init__(self):

        print ('==============================================')
        print ('Simple mockup of 2048 game, made by Heejong Ahn')
        print ('You can see the full code in github.com/heejongahn')
        print ('==============================================')
        print ('\n')

        self.size = int(input('Size of the table? '))
        self.table = self.makeTable()
        self.freeList = list(range(1,16))

        self.printTable()

    # function makeTable
    # Makes a size*size size game table and return it

    def makeTable(self):
        size = self.size

        table = [0] * size
        for i in range(size):
            table[i] = ['-'] * size
        table[0][0] = 2
        return table

    # function printTable
    # Prints current game table state

    def printTable(self):
        table = self.table

        for line in table:
            for e in line:
                val = str(e)
                blank = " " * (4-len(val))
                tile = val + blank
                print (tile, end=" ")
            print ('\n')
        return

    # function pickGrid
    # Pick a free grid from a table and place [2] tile

    def pickGrid(self):
        size = self.size

        grid = random.choice(self.freeList)
        self.freeList.remove(grid)
        self.table[grid//size][grid%size] = 2

    # function makeMove
    # This is what 2048 is about!

    def makeMove(self, usrInput):
        if usrInput == 'w':
            self.moveUp()
        elif usrInput == 's':
            self.moveDown()
        elif usrInput == 'a':
            self.moveLeft()
        elif usrInput == 'd':
            self.moveRight()
        else:
            print ('Please select a valid move')
            return 1
        return 0

    # funciton moveUp
    # Like other three move functions below,
    # 1) Handles the merge first and then
    # 2) Handles the blanks

    def moveUp(self):
        n = self.size
        table = self.table
        freeList = self.freeList

        for col in range(0, n):
            for i in range(0, n-1):
                for j in range(i+1, n):
                    if table[i][col]!= '-' and table[i][col] == table[j][col]:
                        table[j][col] = '-'
                        freeList.append(j*n + col)
                        table[i][col] = table[i][col] * 2
                        break

            for i in range(0, n-1):
                for j in range(i+1, n):
                    if table[i][col]== '-' and table[j][col]!= '-':
                        table[i][col] = table[j][col]
                        table[j][col] = '-'
                        freeList.append(j*n + col)
                        freeList.remove(i*n + col)
                        break


# Main routine

table = Table()

while (table.freeList!= []):
    usrInput = input("Pick a move : w(up) / s(down) / a(left) / d(right) ")
    if table.makeMove(usrInput):
        continue
    table.pickGrid()
    table.printTable()
