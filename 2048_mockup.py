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
        self.freeList = list(range(1,self.size*self.size))
        self.point = 0

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
        print ("Current point is: ", end=" ")
        print (self.point)
        return

    # function pickGrid
    # Pick a free grid from a table and place [2] tile

    def pickGrid(self):
        size = self.size
        candidates = [2,2,2,2,2,2,2,2,2,4]

        grid = random.choice(self.freeList)
        value = random.choice(candidates)

        self.freeList.remove(grid)
        self.table[grid//size][grid%size] = value

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

    # function moveUp
    # Like other three move functions below,
    # 1) Handles the merge first and then
    # 2) Handles the blanks

    def moveUp(self):
        n = self.size
        table = self.table
        freeList = self.freeList

        for col in range(0, n):
            for i in range(0, n-1):
                if table[i][col]!= '-':
                    for j in range(i+1, n):
                        if table[i][col] == table[j][col]:
                            table[j][col] = '-'
                            freeList.append(j*n + col)
                            table[i][col] = table[i][col] * 2
                            self.point += table[i][col]
                            break
                        elif table[j][col] != '-':
                            break

            for i in range(0, n-1):
                if table[i][col] == '-':
                    for j in range(i+1, n):
                        if table[j][col]!= '-':
                            table[i][col] = table[j][col]
                            table[j][col] = '-'
                            freeList.append(j*n + col)
                            freeList.remove(i*n + col)
                            break

    # function moveDown

    def moveDown(self):
        n = self.size
        table = self.table
        freeList = self.freeList

        for col in range(0, n):
            iRange = list(range(1, n))
            iRange.reverse()

            for i in iRange:
                if table[i][col] != '-':
                    jRange = list(range(0, i))
                    jRange.reverse()
                    for j in jRange:
                        if table[i][col] == table[j][col]:
                            table[j][col] = '-'
                            freeList.append(j*n + col)
                            table[i][col] = table[i][col] * 2
                            self.point += table[i][col]
                            break
                        elif table[j][col] != '-':
                            break

            for i in iRange:
                if table[i][col] == '-':
                    jRange = list(range(0, i))
                    jRange.reverse()
                    for j in jRange:
                        if table[j][col]!= '-':
                            table[i][col] = table[j][col]
                            table[j][col] = '-'
                            freeList.append(j*n + col)
                            freeList.remove(i*n + col)
                            break

    def moveLeft(self):
        n = self.size
        table = self.table
        freeList = self.freeList

        for row in range(0, n):
            for i in range(0, n-1):
                if table[row][i] != '-':

                    for j in range(i+1, n):
                        if table[row][i] == table[row][j]:
                            table[row][j] = '-'
                            freeList.append(row*n + j)
                            table[row][i] = table[row][i] * 2
                            self.point += table[row][i]
                            break
                        elif table[row][j] != '-':
                            break

            for i in range(0, n-1):
                if table[row][i] == '-':
                    jRange = list(range(0, i))
                    jRange.reverse()

                    for j in range(i+1, n):
                        if table[row][j]!= '-':
                            table[row][i] = table[row][j]
                            table[row][j] = '-'
                            freeList.append(row*n + j)
                            freeList.remove(row*n + i)
                            break

    def moveRight(self):
        n = self.size
        table = self.table
        freeList = self.freeList

        for row in range(0, n):
            iRange = list(range(1,n))
            iRange.reverse()
            for i in iRange:
                if table[row][i] != '-':
                    jRange = list(range(0, i))
                    jRange.reverse()

                    for j in jRange:
                        if table[row][i] == table[row][j]:
                            table[row][j] = '-'
                            freeList.append(row*n + j)
                            table[row][i] = table[row][i] * 2
                            self.point += table[row][i]
                            break
                        elif table[row][j] != '-':
                            break

            for i in iRange:
                if table[row][i] == '-':
                    jRange = list(range(0, i))
                    jRange.reverse()

                    for j in jRange:
                        if table[row][j]!= '-':
                            table[row][i] = table[row][j]
                            table[row][j] = '-'
                            freeList.append(row*n + j)
                            freeList.remove(row*n + i)
                            break

# Main routine

table = Table()

while (table.freeList!= []):
    usrInput = input("Pick a move : w(up) / s(down) / a(left) / d(right) ")
    if table.makeMove(usrInput):
        continue
    table.pickGrid()
    table.printTable()
