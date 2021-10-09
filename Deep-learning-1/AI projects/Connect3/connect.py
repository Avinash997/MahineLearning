import Tkinter
import turtle

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

def getPos(x,y):
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

	if x<0 and x>-40 and y>40 and y<80:
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

    if x<40 and x>0 and y>40 and y<80:
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
	if x <80 and x >40 and y > 40 and y < 80:
		va2 = 5
		for i in range(0, 4):
			if arr[i][3] == 0:
				va2 = i
				arr[i][3] = -1
				break
		if va2 >= 0 or va2 < 4:
			mypen.color("black", "red")
			mypen.begin_fill()
			mypen.up()
			mypen.goto(60,(-40)*(va2 - 1))
			mypen.down()
			mypen.circle(20)
			mypen.end_fill()

def main():
	turtle.onscreenclick(getPos)

main()
Tkinter.mainloop()