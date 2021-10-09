#ID NUMBER 2015A7PS0103P
#NAME - AMAN RAJ
import turtle as t
import random

from turtle import Turtle, Screen
#Set up Screen
wn = t.Screen()

#Draw border
mypen = t.Turtle()
mypen.penup()
posx = -200
posy = -200
mypen.setposition(posx,posy)
mypen.pendown()
mypen.pensize(3)
mypen.speed(0)
for side in range(10):
    mypen.forward(400)
    mypen.left(90)
    mypen.forward(40)
    mypen.left(90)
    mypen.forward(400)
    mypen.left(90)
    mypen.forward(40)
    mypen.left(90)
    mypen.penup()
    posy = posy+40
    mypen.setposition(posx,posy)
    mypen.pendown()
mypen.penup()
posx = -160
posy= -200
mypen.setposition(posx,posy)
mypen.left(90)
mypen.pendown()
for side in range(9):
    mypen.forward(400)
    mypen.right(90)
    mypen.penup()
    mypen.forward(40)
    mypen.right(90)
    mypen.pendown()
    mypen.forward(400)
    mypen.right(180)


mypen.penup()
posx = -180
posy = 180
mypen.setposition(-180,180)
mypen.pendown()
mypen.right(90)

#random array generating the dirt
array=[0]*100
i1=random.randint(0,100)
for j in range(i1):
    k = random.randint(0, 99)
    array[k]=1
print array

#if there is dirt on the corresponding below element of the array,
#  it goes and cleans it and returns back to initial position
for i in range(0,80):
    for j in range(10):
        if(array[j+i+10] == 1):
            mypen.right(90)
            mypen.forward(40)
            mypen.right(180)
            mypen.forward(40)
            mypen.right(90)
        if((j+i+1)%10==0):
            mypen.penup()
            posy = posy-80
            mypen.setposition(posx,posy)
            mypen.pendown()
        mypen.forward(40)
    i = i+19



t.exitonclick()
