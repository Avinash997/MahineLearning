#importing all necessary packages
import time
import Tkinter
import turtle
from copy import copy,deepcopy

#Declares an array which defines a state
#nodes defines the number of nodes created while executing
nodes = 0
arr=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#Make Screen
mypen=turtle.Pen()
mypen.hideturtle()
mypen.speed(0)
mypen.up()
mypen.setposition(-80,-80)
mypen.down()
for i in range(5):
    mypen.left(90)
    mypen.fd(160)
    mypen.up()
    mypen.bk(160)
    mypen.rt(90)
    mypen.fd(40)
    mypen.down()
mypen.up()
mypen.goto(-80,-80)
mypen.down()
for i in range(5):
    mypen.forward(160)
    mypen.up()
    mypen.bk(160)
    mypen.left(90)
    mypen.forward(40)
    mypen.right(90)
    mypen.down()
mypen.up()
mypen.goto(-80,88)
mypen.down()
mypen.color("blue")
mypen.width(3)
mypen.forward(160)
mypen.width(1)
#mypen.write("Base Line")

#Defines Action on Screen Click
def position(x,y):
    global arr
    if x<-40 and x>-80 and y>40 and y<80:
        va=5
        for i in range(0,4):
            if arr[i][0]==0:
                va=i
                arr[i][0]=-1
                break
        if va>=0 and va<4:
            mypen.color("black", "red")
            mypen.begin_fill()
            mypen.up()
            mypen.goto(-60,(-40)*(va-1))
            mypen.down()
            mypen.circle(20)
            mypen.end_fill()

    elif x<0 and x>-40 and y>40 and y<80:
        va3=5
        for i in range(0,4):
            if arr[i][1]==0:
                va3=i
                arr[i][1]=-1
                break
        if va3>=0 and va3<4:
            mypen.color("black", "red")
            mypen.begin_fill()
            mypen.up()
            mypen.goto(-20,(-40)*(va3-1))
            mypen.down()
            mypen.circle(20)
            mypen.end_fill()

    elif x<40 and x>0 and y>40 and y<80:
        va1=5
        for i in range(0,4):
            if arr[i][2]==0:
                va1=i
                arr[i][2]=-1
                break
        if va1>=0 and va1<4:
            mypen.color("black", "red")
            mypen.begin_fill()
            mypen.up()
            mypen.goto(20,(-40)*(va1-1))
            mypen.down()
            mypen.circle(20)
            mypen.end_fill()

    elif x <80 and x >40 and y > 40 and y < 80:
        va2 = 5
        for i in range(0, 4):
            if arr[i][3] == 0:
                va2 = i
                arr[i][3] = -1
                break
        if va2 >= 0 and va2 < 4:
            mypen.color("black", "red")
            mypen.begin_fill()
            mypen.up()
            mypen.goto(60,(-40)*(va2 - 1))
            mypen.down()
            mypen.circle(20)
            mypen.end_fill()
    else:
        turtle.onscreenclick(position)

    print arr
    if (terminalTest(arr) != 0):
        print "Player Wins"
        exit(0)
    if (fullBoard(arr) == 1):
        print "Draw"
        exit(0)
    arr = minimaxDecision(arr)
    print nodes
    print arr
    if (terminalTest(arr) != 0):
        print "Machine Wins"
        exit(0)
    turtle.onscreenclick(position)


#Defines Terminal Conditions
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

#Checks full Board condition
def  fullBoard(arr):
    for i in range (0,4):
        for j in range (0,4):
            if arr[i][j]==0:
                return 0
    return 1

#Generates all sucessor states
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

#maxValue function
def maxValue(arr1):
    global nodes
    val1 = 1
    if (terminalTest(arr1) != 0):
        return terminalTest(arr1)
    if(fullBoard(arr1)==1):
        return 0
    val = -999
    for i in sucAction(arr1,val1):
        nodes = nodes+1
        temp = minValue(i)
        if (temp> val):
            val = temp
    return val

#minValue function
def minValue(arr1):
    global nodes
    val2 = -1
    if(terminalTest(arr1)!=0):
        return terminalTest(arr1)
    if(fullBoard(arr1)==1):
        return 0
    val = 999
    for i in sucAction(arr1,val2):
        nodes = nodes+1
        temp = maxValue(i)
        if(temp<val):
            val = temp
    return val

#minimax function in which a 2-D array is used to represent a state
def minimaxDecision(arr):
    global nodes
    val1 = 1
    z = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    succ = sucAction(arr,val1)
    val = -999
    for i in succ:
        nodes = nodes+1
        temp =minValue(i)
        if temp>val:
            val=temp
            z = deepcopy(i)
    mark(arr,z)
    arr = z
    return arr

#marks the corresponding slot in the GUI
def mark(arr,irr):
    x=0
    y=0
    for i in range (0,4):
        for j in range (0,4):
            if(arr[i][j]!=irr[i][j]):
                y=i
                x=j
                break
    if(x==0):
        mypen.color("black", "black")
        mypen.begin_fill()
        mypen.up()
        mypen.goto(-60,(-40)*(y-1))
        mypen.down()
        mypen.circle(20)
        mypen.end_fill()
    if(x==1):
        mypen.color("black", "black")
        mypen.begin_fill()
        mypen.up()
        mypen.goto(-20, (-40) * (y - 1))
        mypen.down()
        mypen.circle(20)
        mypen.end_fill()
    if(x==2):
        mypen.color("black", "black")
        mypen.begin_fill()
        mypen.up()
        mypen.goto(20, (-40) * (y - 1))
        mypen.down()
        mypen.circle(20)
        mypen.end_fill()
    if(x==3):
        mypen.color("black", "black")
        mypen.begin_fill()
        mypen.up()
        mypen.goto(60, (-40) * (y - 1))
        mypen.down()
        mypen.circle(20)
        mypen.end_fill()

def main():
    global arr
    i=deepcopy(arr)
    i[0][0]=1
    mark(arr,i)
    arr = deepcopy(i)
    print arr
    if(terminalTest(arr)!=0):
        print "Machine Wins"
    turtle.onscreenclick(position)


main()

Tkinter.mainloop()