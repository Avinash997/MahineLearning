import turtle as t
import Tkinter

from time import sleep
from turtle import Turtle, Screen
#Set up Screen
wn = t.Screen()

pen=t.Pen()
def getPos(x,y):
    pen.up()
    if (x > -80 and x < -40 and y > -80 and y < -40):
        pen.setposition(-60, -60)
        arr[0][0]=1
    if (x > -80 and x < -40 and y > -40 and y < 0):
        pen.setposition(-60, -20)
        arr[1][0]=1
    if (x > -80 and x < -40 and y > 0 and y < 40):
        pen.setposition(-60, 20)
        arr[2][0] = 1
    if (x > -80 and x < -40 and y > 40 and y < 80):
        pen.setposition(-60, 60)
        arr[3][0] = 1
    if (x > -40 and x < 0 and y > -80 and y < -40):
        pen.setposition(-20, -60)
        arr[0][1] = 1
    if (x > -40 and x < 0 and y > -40 and y < 0):
        pen.setposition(-20, -20)
        arr[1][1] = 1
    if (x > -40 and x < 0 and y > 0 and y < 40):
        pen.setposition(-20, 20)
        arr[2][1] = 1
    if (x > -40 and x < 0 and y > 40 and y < 80):
        pen.setposition(-20, 60)
        arr[3][1] = 1
    if (x > 0 and x < 40 and y > -80 and y < -40):
        pen.setposition(20, -60)
        arr[0][2] = 1
    if (x > 0 and x < 40 and y > -40 and y < 0):
        pen.setposition(20, -20)
        arr[1][2] = 1
    if (x > 0 and x < 40 and y > 0 and y < 40):
        pen.setposition(20, 20)
        arr[2][2] = 1
    if (x > 0 and x < 40 and y > 40 and y < 80):
        pen.setposition(20, 60)
        arr[3][2] = 1
    if (x > 40 and x < 80 and y > -80 and y < -40):
        pen.setposition(60, -60)
        arr[0][3] = 1
    if (x > 40 and x < 80 and y > -40 and y < 0):
        pen.setposition(60, -20)
        arr[1][3] = 1
    if (x > 40 and x < 80 and y > 0 and y < 40):
        pen.setposition(60, 20)
        arr[2][3] = 1
    if (x > 40 and x < 80 and y > 40 and y < 80):
        pen.setposition(60, 60)
        arr[3][3] = 1
    pen.down()
    pen.color("green")
    pen.circle(20)
    pen.up()

def player(turn):
    if(turn%2==0):
        return 2
    else:
        return 1

def initialize(arr):
    for i in range (4):
        for j in range (4):
            arr[i][j]=0
#A double dimensional array
width,height=4,4
arr = [[0 for x in range(width)] for y in range(height)]
initialize(arr)

#Defines the terminal tests for the game
def terminalTest(arr):
    for i in range (4):
        if(arr[i][0]==arr[i][1] & arr[i][1]==arr[i][2] & arr[i][0]!=0):
            return 1
        if(arr[i][1]==arr[i][2] & arr[i][2]==arr[i][3] & arr[i][1]!=0):
            return 1
    for i in range(4):
        if (arr[0][i] == arr[1][i] & arr[1][i] == arr[2][i] & arr[0][i] != 0):
            return 1
        if (arr[1][i] == arr[2][i] & arr[2][i] == arr[3][i] & arr[1][i] != 0):
            return 1
    for i in range(2):
        if (arr[i][i] == arr[i+1][i+1] & arr[i+1][i+1] == arr[i+2][i+2] & arr[i][i] != 0):
            return 1
    for i in range(2):
        if (arr[i][3-i] == arr[i+1][2-i] & arr[i+1][2-i] == arr[i+2][1-i] & arr[i][3-i] != 0):
            return 1
    if(arr[0][1]==arr[1][2] & arr[1][2]==arr[2][3] & arr[0][1]!=0):
        return 1
    if(arr[1][0]==arr[2][1] & arr[2][1]==arr[3][2] & arr[1][0]!=0):
        return 1
    if(arr[0][2]==arr[1][1] & arr[1][1]==arr[2][0] & arr[0][2]!=0):
        return 1
    if(arr[1][3]==arr[2][2] & arr[2][2]==arr[3][1] & arr[2][2]!=0):
        return 1
    return 0


#def action(arr):
def gotoandprint(x, y):
    turtle1=t.Turtle()
    turtle1.penup()
    gotoresult = turtle1.goto(x, y)
    if (turtle1.xcor() > -80 and turtle1.xcor() < -40 and turtle1.ycor() > -80 and turtle1.ycor() < -40):
        turtle1.setposition(-60, -60)
        arr[0][0]=1
    if (turtle1.xcor() > -80 and turtle1.xcor() < -40 and turtle1.ycor() > -40 and turtle1.ycor() < 0):
        turtle1.setposition(-60, -20)
        arr[1][0]=1
    if (turtle1.xcor() > -80 and turtle1.xcor() < -40 and turtle1.ycor() > 0 and turtle1.ycor() < 40):
        turtle1.setposition(-60, 20)
        arr[2][0] = 1
    if (turtle1.xcor() > -80 and turtle1.xcor() < -40 and turtle1.ycor() > 40 and turtle1.ycor() < 80):
        turtle1.setposition(-60, 60)
        arr[3][0] = 1
    if (turtle1.xcor() > -40 and turtle1.xcor() < 0 and turtle1.ycor() > -80 and turtle1.ycor() < -40):
        turtle1.setposition(-20, -60)
        arr[0][1] = 1
    if (turtle1.xcor() > -40 and turtle1.xcor() < 0 and turtle1.ycor() > -40 and turtle1.ycor() < 0):
        turtle1.setposition(-20, -20)
        arr[1][1] = 1
    if (turtle1.xcor() > -40 and turtle1.xcor() < 0 and turtle1.ycor() > 0 and turtle1.ycor() < 40):
        turtle1.setposition(-20, 20)
        arr[2][1] = 1
    if (turtle1.xcor() > -40 and turtle1.xcor() < 0 and turtle1.ycor() > 40 and turtle1.ycor() < 80):
        turtle1.setposition(-20, 60)
        arr[3][1] = 1
    if (turtle1.xcor() > 0 and turtle1.xcor() < 40 and turtle1.ycor() > -80 and turtle1.ycor() < -40):
        turtle1.setposition(20, -60)
        arr[0][2] = 1
    if (turtle1.xcor() > 0 and turtle1.xcor() < 40 and turtle1.ycor() > -40 and turtle1.ycor() < 0):
        turtle1.setposition(20, -20)
        arr[1][2] = 1
    if (turtle1.xcor() > 0 and turtle1.xcor() < 40 and turtle1.ycor() > 0 and turtle1.ycor() < 40):
        turtle1.setposition(20, 20)
        arr[2][2] = 1
    if (turtle1.xcor() > 0 and turtle1.xcor() < 40 and turtle1.ycor() > 40 and turtle1.ycor() < 80):
        turtle1.setposition(20, 60)
        arr[3][2] = 1
    if (turtle1.xcor() > 40 and turtle1.xcor() < 80 and turtle1.ycor() > -80 and turtle1.ycor() < -40):
        turtle1.setposition(60, -60)
        arr[0][3] = 1
    if (turtle1.xcor() > 40 and turtle1.xcor() < 80 and turtle1.ycor() > -40 and turtle1.ycor() < 0):
        turtle1.setposition(60, -20)
        arr[1][3] = 1
    if (turtle1.xcor() > 40 and turtle1.xcor() < 80 and turtle1.ycor() > 0 and turtle1.ycor() < 40):
        turtle1.setposition(60, 20)
        arr[2][3] = 1
    if (turtle1.xcor() > 40 and turtle1.xcor() < 80 and turtle1.ycor() > 40 and turtle1.ycor() < 80):
        turtle1.setposition(60, 60)
        arr[3][3] = 1

def main():
#Draw border
    mypen = t.Turtle()
    mypen.penup()
    posx = -80
    posy = -80
    mypen.setposition(posx,posy)
    mypen.pendown()
    mypen.pensize(3)
    mypen.speed(0)
    for side in range(4):
        mypen.forward(160)
        mypen.left(90)
        mypen.forward(40)
        mypen.left(90)
        mypen.forward(160)
        mypen.left(90)
        mypen.forward(40)
        mypen.left(90)
        mypen.penup()
        posy = posy+40
        mypen.setposition(posx,posy)
        mypen.pendown()
    mypen.penup()
    posx = -40
    posy= -80
    mypen.setposition(posx,posy)
    mypen.left(90)
    mypen.pendown()
    for side in range(3):
        mypen.forward(160)
        mypen.right(90)
        mypen.penup()
        mypen.forward(40)
        mypen.right(90)
        mypen.pendown()
        mypen.forward(160)
        mypen.right(180)

    mypen.penup()
    mypen.setposition(-80,-80)
    mypen.right(90)
    mypen.pendown()
    mypen.hideturtle()



#Game starts with first move of the person
    #while True:
    #turtle1 = t.Turtle()
    #turtle1.penup()
    #screen = Screen()
    #screen.onscreenclick(gotoandprint)
    #print(arr)

    #getcoord()
    #print (arr)
    t.onscreenclick(getPos)

    Tkinter.mainloop()
    t.exitonclick()

main()