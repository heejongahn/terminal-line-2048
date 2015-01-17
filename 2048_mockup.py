import random

print '=============================================='
print 'Simple mockup of 2048 game, made by Heejong Ahn'
print 'You can see the code in github.com/heejongahn'
print '=============================================='

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
            print e,
        print '\n'

table = makeTable(n)
printTable(table)
