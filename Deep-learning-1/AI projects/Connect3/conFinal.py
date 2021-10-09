import turtle
import Tkinter


arr=[['e','e','e','e'],['e','e','e','e'],['e','e','e','e'],['e','e','e','e']]
pen=turtle.Pen()
pen.hideturtle()
pen.speed(0)
pen.up()
pen.goto(-200,-200)
pen.down()
for i in range(5):
    pen.left(90)
    pen.fd(400)
    pen.up()
    pen.bk(400)
    pen.rt(90)
    pen.fd(100)
    pen.down()
pen.up()
pen.goto(-200,-200)
pen.down()
for i in range(5):
    pen.forward(400)
    pen.up()
    pen.bk(400)
    pen.left(90)
    pen.forward(100)
    pen.right(90)
    pen.down()
pen.up()
pen.goto(-200,220)
pen.down()
pen.color("red")
pen.width(5)
pen.forward(400)
pen.width(1)
#pen.write("Base Line")

def getPos(x,y):
    if x<-100 and x>-200 and y>100 and y<200:
        val=5
        for i in range(0,4):
            if arr[i][0]=='e':
                val=i
                arr[i][0]='h'
                break
        if val>=0 or val<4:
            pen.color("black", "blue")
            pen.begin_fill()
            pen.up()
            pen.goto(-150,(val-1)*(-100))
            pen.down()
            pen.circle(50)
            pen.end_fill()

    if x<-0 and x>-100 and y>100 and y<200:
        val=5
        for i in range(0,4):
            if arr[i][1]=='e':
                val=i
                arr[i][1]='h'
                break
        if val>=0 or val<4:
            pen.color("black", "blue")
            pen.begin_fill()
            pen.up()
            pen.goto(-50,(val-1)*(-100))
            pen.down()
            pen.circle(50)
            pen.end_fill()

    if x<100 and x>0 and y>100 and y<200:
        val=5
        for i in range(0,4):
            if arr[i][2]=='e':
                val=i
                arr[i][2]='h'
                break
        if val>=0 or val<4:
            pen.color("black", "blue")
            pen.begin_fill()
            pen.up()
            pen.goto(50,(val-1)*(-100))
            pen.down()
            pen.circle(50)
            pen.end_fill()

    if x<200 and x>100 and y>100 and y<200:
        val=5
        for i in range(0,4):
            if arr[i][3]=='e':
                val=i
                arr[i][3]='h'
                break
        if val>=0 or val<4:
            pen.color("black", "blue")
            pen.begin_fill()
            pen.up()
            pen.goto(150,(val-1)*(-100))
            pen.down()
            pen.circle(50)
            pen.end_fill()

def main()
