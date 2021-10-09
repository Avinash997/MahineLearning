import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def callBack(nam1):
   print nam1

lbl= Tkinter.Label(top, text='Query Variables', fg='purple', bg='turquoise', font=('comicsans', 10))
lbl.place(x=30,y=0)
lb2= Tkinter.Label(top, text='Condition Variables', fg='purple', bg='turquoise', font=('comicsans', 10))
lb2.place(x=300,y=0)
def makerow(x1,y1,nam):
   MyButton1 = Tkinter.Button(top, text=nam, width=2, command=lambda: callBack(nam))
   MyButton1.place(x=x1,y=y1) #30,40

   MyButton2 = Tkinter.Button(top, text=("~" + nam), width=2, command=lambda: callBack("~" + nam))
   MyButton2.place(x=x1+50, y=y1)

   MyButton3 = Tkinter.Button(top, text=nam, width=2, command=lambda: callBack(nam))
   MyButton3.place(x=x1+270, y=y1)

   MyButton3 = Tkinter.Button(top, text=("~" + nam), width=2, command=lambda: callBack("~"+nam))
   MyButton3.place(x=x1+320, y=y1)

def main():
   j=30
   k=40
   for i in range (0,10):
      makerow(j,k,"A")
      k=k+20

main()

top.mainloop()