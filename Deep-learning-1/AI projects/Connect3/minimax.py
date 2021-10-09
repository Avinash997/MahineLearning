#Defines the terminal tests for the game
#Assumes machine as -1 and player as 1
from copy import copy,deepcopy
#A double dimensional array


def initialize(arr):
    for i in range (4):
        for j in range (4):
            arr[i][j]=0


width,height=4,4
arr = [[0 for x in range(width)] for y in range(height)]
initialize(arr)


def terminalTest(arr):
    for i in range (4):
        if(arr[i][0]==arr[i][1] and arr[i][1]==arr[i][2] and arr[i][0]!=0):
            return arr[i][0]
        if(arr[i][1]==arr[i][2] and arr[i][2]==arr[i][3] and arr[i][1]!=0):
            return arr[i][1]
    for i in range(4):
        if (arr[0][i] == arr[1][i] and arr[1][i] == arr[2][i] and arr[0][i] != 0):
            return arr[0][i]
        if (arr[1][i] == arr[2][i] and arr[2][i] == arr[3][i] and arr[1][i] != 0):
            return arr[1][i]
    for i in range(2):
        if (arr[i][i] == arr[i+1][i+1] and arr[i+1][i+1] == arr[i+2][i+2] and arr[i][i] != 0):
            return arr[i][i]
    for i in range(2):
        if (arr[i][3-i] == arr[i+1][2-i] and arr[i+1][2-i] == arr[i+2][1-i] and arr[i][3-i] != 0):
            return arr[i][3-i]
    if(arr[0][1]==arr[1][2] and arr[1][2]==arr[2][3] and arr[0][1]!=0):
        return arr[0][1]
    if(arr[1][0]==arr[2][1] and arr[2][1]==arr[3][2] and arr[1][0]!=0):
        return arr[1][0]
    if(arr[0][2]==arr[1][1] and arr[1][1]==arr[2][0] and arr[0][2]!=0):
        return arr[0][2]
    if(arr[1][3]==arr[2][2] and arr[2][2]==arr[3][1] and arr[2][2]!=0):
        return arr[1][3]
    return 0


def  fullBoard(arr):
    for i in range (0,4):
        for j in range (0,4):
            if arr[i][j]==0:
                return 0
    return 1

def sucAction(arr,val):
    c=[]
    for i in range(0,4):
        z = deepcopy(arr)
        for j in range (0,4):
            if z[j][i] == 0:
                z[j][i]=val
                c.append(z)
                break
    return c


def maxValue(arr1):
    val1 = 1
    if (terminalTest(arr1) != 0):
        return terminalTest(arr1)
    if(fullBoard(arr1)==1):
        return 0
    val = -999
    for i in sucAction(arr1,val1):
        if (minValue(i)> val):
            val = minValue(i)
    return val


def minValue(arr1):
    val2 = -1
    if(terminalTest(arr1)!=0):
        return terminalTest(arr1)
    if(fullBoard(arr1)==1):
        return 0
    val = 999
    for i in sucAction(arr1,val2):
        if(maxValue(i)<val):
            val = maxValue(i)
            break
    return val


def minimaxDecision(arr):
    val1 = 1
    succ = sucAction(arr,val1)
    val = -999
    for i in succ:
        temp =minValue(i)
        if temp>val:
            val=temp
            arr = deepcopy(i)
    return arr


def main():
    global arr
    while True:
        arr = minimaxDecision(arr)
        print arr
        if(terminalTest(arr)!=0):
            print "Machine Wins"
            break
        column = int(raw_input("Enter a column: "))
        for i in range (0,4):
            if arr[i][column]==0:
                arr[i][column]=-1
                break
        print arr
        if(terminalTest(arr)!=0):
            print "Player Wins"
            break
        if(fullBoard(arr)==1):
            print "Draw"
            break


main()

