import csv
import random
cour = ['C_01']
for i in range(2,51):
    s = 'C_'
    if i<=9:
        s = s+'0'+str(i)
    else:
        s = s+str(i)
    cour.append(s)
#print cour
ctype1 = ['DC']
ctype2 = ['GE']
ctype3 = ['DE']
L = [3]
T = [0]
P = [2]
for i in range(2,51):
    s = random.randint(0,1)
    if(i==10) or (i==20):
        ctype1.append('DC')
    else:
        if s==0:
            ctype1.append('GE')
        else:
            ctype1.append('DE')

for i in range(2,51):
    s = random.randint(0,1)
    if(i==5) or (i==15) or (i==35):
        ctype2.append('DC')
    else:
        if s==0:
            ctype2.append('GE')
        else:
            ctype2.append('DE')

for i in range(2,51):
    s = random.randint(0,1)
    if(i==25) or (i==30) or (i==37):
        ctype3.append('DC')
    else:
        if s==0:
            ctype3.append('GE')
        else:
            ctype3.append('DE')

for i in range(2,51):
    s = random.randint(2,3)
    if s==2:
        L.append(2)
    else:
        L.append(3)

for i in range(2,51):
    s = random.randint(0,1)
    T.append(s)

for i in range(2,51):
    s = random.randint(0,3)
    P.append(s)

prof = ['P_01']
for i in range(2,21):
    s = 'P_'
    if i<=9:
        s = s+'0'+str(i)
    else:
        s = s+str(i)
    prof.append(s)

cte1 = ['C_01','C_10','C_20']
cte2 = ['C_11','C_15','C_17']
cte3 = ['C_15','C_05','C_35']
cte4 = ['C_30','C_37','C_25']

for i in range(4,21):
    s = 'C_'
    s2 = random.randint(1,50)
    if s2<=9:
        s =s + '0' + str(s2)
    else:
        s=s+str(s2)
    cte1.append(s)

for i in range(4,21):
    s = 'C_'
    s2 = random.randint(1,50)
    if s2<=9:
        s =s + '0' + str(s2)
    else:
        s=s+str(s2)
    cte2.append(s)

for i in range(4,21):
    s = 'C_'
    s2 = random.randint(1,50)
    if s2<=9:
        s =s + '0' + str(s2)
    else:
        s=s+str(s2)
    cte3.append(s)

for i in range(4,21):
    s = 'C_'
    s2 = random.randint(1,50)
    if s2<=9:
        s =s + '0' + str(s2)
    else:
        s=s+str(s2)
    cte4.append(s)



with open('courses.csv','w') as new_file:
    csv_writer = csv.writer(new_file, delimiter=',')

    line = ['Course','Prog A','Prog B','Prog C','L','T','P']
    csv_writer.writerow(line)

    for i in range (0,50):
        line = [cour[i],ctype1[i],ctype2[i],ctype3[i],str(L[i]),str(T[i]),str(P[i])]
        csv_writer.writerow(line)

with open('prof.csv','w') as n_file:
    csv_write = csv.writer(n_file, delimiter=',')

    line = ['Professor','Course1','Course2','Course3','Course4']
    csv_write.writerow(line)

    for i in range (0,20):
        line = [prof[i],cte1[i],cte2[i],cte3[i],cte4[i]]
        csv_write.writerow(line)

