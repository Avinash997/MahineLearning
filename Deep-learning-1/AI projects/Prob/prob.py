import Tkinter
import tkMessageBox
import itertools
import copy

top = Tkinter.Tk()
querylist = []
conditionlist = []
variablelist = []
def callBack(Button1,nam1,index):
    Button1.configure(bg = 'yellow')
    if index == 1:
        if nam1 not in querylist:
            querylist.append(nam1)
    else:
        if nam1 not in conditionlist:
            conditionlist.append(nam1)

def toint(y,index):
    decimal = 0
    for digit in y:
        decimal = decimal * index + int(digit)
    return decimal

def compute(flist):
    global fulladlist
    prod = 1.0
    for var in flist:
        if var[0]=='~':
            for line in fulladlist:
                if line[0]==var[1]:
                    par=copy.deepcopy(line[1])
                    s = ''
                    for p in par:
                        if p in flist:
                            s=s+'1'
                        else:
                            s=s+'0'
                    c = toint(s, 2)
                    valn = line[2][c]
                    prod=prod*(1-valn)
                    break
        else:
            for line in fulladlist:
                if line[0]==var:
                    par = copy.deepcopy(line[1])
                    s=''
                    for p in par:
                        if p in flist:
                            s=s+'1'
                        else:
                            s=s+'0'
                    c=toint(s, 2)
                    valn = line[2][c]
                    prod=prod*valn
                    break
    return prod

def computeprob(plist):
    slist = []
    for i in plist:
        if i[0]=='s':
            slist.append(i)
    nslist = []
    for i in plist:
        if i[0]!='s':
            nslist.append(i)
    poss = list(map(list, itertools.product([0, 1], repeat=len(slist))))
    sum = 0.0
    for i in range(len(poss)):
        salist = []
        comb = poss[i]
        k=0
        for j in slist:
            if comb[k]==0:
                salist.append('~'+j[1])
            else:
                salist.append(j[1])
            k=k+1
        nalist = copy.deepcopy(nslist)
        nalist.extend(salist)
        #print nalist
        #print nslist
        sum=sum+compute(nalist)
    return sum




def aftermain():
    lbl = Tkinter.Label(top, text='Generated Query', fg='purple', bg='turquoise', font=('comicsans', 10))
    lbl.place(x=100,y=450)
    st = 'P('
    for i in querylist:
        st = st+i+','
    if conditionlist is None:
        b_s = bytearray(st)
        b_s[len(st)-1] = ')'
        st = str(b_s)
    else:
        b_s = bytearray(st)
        b_s[len(st) - 1] = '|'
        st = str(b_s)
        for i in conditionlist:
            st = st +i+','
        b_s = bytearray(st)
        b_s[len(st) - 1] = ')'
        st = str(b_s)
    lb2 = Tkinter.Label(top, text=st, fg='red', bg='turquoise', font=('comicsans', 10))
    lb2.place(x=250,y=450)
    plist=copy.deepcopy(querylist)
    plist.extend(conditionlist)
    for i in variablelist:
        if i in plist or ('~'+i) in plist:
            continue
        else:
            plist.append('s'+i)
    plist = list(set(plist))
    s1=computeprob(plist)
    clist = copy.deepcopy(conditionlist)
    for i in variablelist:
        if i in clist or ('~'+i) in clist:
            continue
        else:
            clist.append('s'+i)
    clist = list(set(clist))
    s2=computeprob(clist)
    s3 = s1/s2
    lb3 = Tkinter.Label(top, text='Answer', fg='purple', bg='turquoise', font=('comicsans', 10))
    lb3.place(x=100,y=500)
    lb4 = Tkinter.Label(top, text=str(s3), fg='purple', bg='turquoise', font=('comicsans', 10))
    lb4.place(x=200,y=500)


lbl= Tkinter.Label(top, text='Query Variables', fg='purple', bg='turquoise', font=('comicsans', 10))
lbl.place(x=30,y=0)
lb2= Tkinter.Label(top, text='Condition Variables', fg='purple', bg='turquoise', font=('comicsans', 10))
lb2.place(x=300,y=0)
finb = Tkinter.Button(top, text="Finish", width=10, command=lambda: aftermain())
finb.place(x=160,y=400)
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def makerow(x1,y1,nam):
   MyButton1 = Tkinter.Button(top, text=nam, width=2, command=lambda: callBack(MyButton1,nam,1))
   MyButton1.place(x=x1,y=y1) #30,40

   MyButton2 = Tkinter.Button(top, text=("~" + nam), width=2, command=lambda: callBack(MyButton2,"~" + nam,1))
   MyButton2.place(x=x1+50, y=y1)

   MyButton3 = Tkinter.Button(top, text=nam, width=2, command=lambda: callBack(MyButton3,nam,2))
   MyButton3.place(x=x1+270, y=y1)

   MyButton4 = Tkinter.Button(top, text=("~" + nam), width=2, command=lambda: callBack(MyButton4,"~"+nam,2))
   MyButton4.place(x=x1+320, y=y1)

fulladlist = []
def createBayesianNetwork():
    readw = open("input1.txt","r")
    for line in readw:
        if line[0]=="$" :
            continue
        point = line[0]
        adlist = []
        for i in range (6,len(line)):
            if line[i]==']':
                break
            else:
                if line[i]!=',' and line[i]!=' ':
                    adlist.append(line[i])
        int_list = []
        for x in line.split():
            if hasNumbers(x):
                int_list.append(float(x))
        pair = []
        pair.append(point)
        pair.append(adlist)
        pair.append(int_list)
        fulladlist.append(pair)

def computeMarkovBlanket(node):
    blank = []
    blank.append(node)
    for line in fulladlist :
        if line[0] == node:
            blank.extend(line[1])
        else:
            if node in line[1]:
                blank.append(line[0])
                for lin1 in fulladlist:
                    if lin1[0] == line[0]:
                        blank.extend(lin1[1])
    blank = list(set(blank))
    return blank

def main():
    createBayesianNetwork()
    #print computeMarkovBlanket('B')
    global fulladlist
    variab = []
    for i in fulladlist:
        variab.append(i[0])
    variab.sort()
    global variablelist
    variablelist = variab
    j=30
    k=40
    for i in variab:
        makerow(j,k,i)
        k=k+20

main()

top.mainloop()