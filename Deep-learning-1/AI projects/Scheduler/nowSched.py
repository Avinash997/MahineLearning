import csv

progADC=[]
progAGE=[]
progADE=[]
progBDC = []
progBGE = []
progBDE = []
progCDC = []
progCGE = []
progCDE = []
combA=[]
combB=[]
combC = []

mytime = 6*[[{'CN':'NO','CT':'NO','CH':'NO','PR':'NO'},{'CN':'NO','CT':'NO','CH':'NO','PR':'NO'},{'CN':'NO','CT':'NO','CH':'NO','PR':'NO'},{'CN':'NO','CT':'NO','CH':'NO','PR':'NO'},
          {'CN': 'NO', 'CT': 'NO', 'CH': 'NO', 'PR': 'NO'},{'CN':'NO','CT':'NO','CH':'NO','PR':'NO'},{'CN':'NO','CT':'NO','CH':'NO','PR':'NO'}]]
def generate_package():
    with open('courses.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            if line[1] == 'DC':
                progADC.append(line[0])
            elif line[1] == 'GE':
                progAGE.append(line[0])
            elif line[1] == 'DE':
                progADE.append(line[0])
            if line[2] == 'DC':
                progBDC.append(line[0])
            elif line[2] == 'GE':
                progBGE.append(line[0])
            elif line[2] == 'DE':
                progBDE.append(line[0])
            if line[3] == 'DC':
                progCDC.append(line[0])
            elif line[3] == 'GE':
                progCGE.append(line[0])
            elif line[3] == 'DE':
                progCDE.append(line[0])
        sizeGE = len(progAGE)
        sizeDE = len(progADE)
        for i in range(0, sizeGE):
            for j in range(i + 1, sizeGE):
                for k in range(0, sizeDE):
                    st = '{' + progADC[0] + ',' + progADC[1] + ',' + progADC[2] + '}' + '{' + progAGE[i] + ',' + progAGE[
                        j] + '}' + '{' + progADE[k] + '}'
                    combA.append(st)
                    print(
                    '{' + progADC[0] + ',' + progADC[1] + ',' + progADC[2] + '}' + '{' + progAGE[i] + ',' + progAGE[
                        j] + '}' + '{' + progADE[k] + '}')
        sizeGE = len(progBGE)
        sizeDE = len(progBDE)
        for i in range(0, sizeGE):
            for j in range(i + 1, sizeGE):
                for k in range(0, sizeDE):
                    st= '{' + progBDC[0] + ',' + progBDC[1] + ',' + progBDC[2] + '}' + '{' + progBGE[i] + ',' + progBGE[
                            j] + '}' + '{' + progBDE[
                            k] + '}'
                    combB.append(st)
                    print(
                        '{' + progBDC[0] + ',' + progBDC[1] + ',' + progBDC[2] + '}' + '{' + progBGE[i] + ',' + progBGE[
                            j] + '}' + '{' + progBDE[
                            k] + '}')
        sizeGE = len(progCGE)
        sizeDE = len(progCDE)
        for i in range(0, sizeGE):
            for j in range(i + 1, sizeGE):
                for k in range(0, sizeDE):
                    st = '{' + progCDC[0] + ',' + progCDC[1] + ',' + progCDC[2] + '}' + '{' + progCGE[i] + ',' + progCGE[
                            j] + '}' + '{' + progCDE[
                            k] + '}'
                    combC.append(st)
                    print(
                        '{' + progCDC[0] + ',' + progCDC[1] + ',' + progCDC[2] + '}' + '{' + progCGE[i] + ',' + progCGE[
                            j] + '}' + '{' + progCDE[
                            k] + '}')


def main():
    generate_package()
    for line in combA:
        courselist = []
        courselist.append(line[1]+line[2]+line[3]+line[4])
        courselist.append(line[6]+line[7]+line[8]+line[9])
        courselist.append(line[11]+line[12]+line[13]+line[14])
        courselist.append(line[17]+line[18]+line[19]+line[20])
        courselist.append(line[22]+line[23]+line[24]+line[25])
        courselist.append(line[28]+line[29]+line[30]+line[31])

    for line in combB:
        courselist = []
        courselist.append(line[1]+line[2]+line[3]+line[4])
        courselist.append(line[6]+line[7]+line[8]+line[9])
        courselist.append(line[11]+line[12]+line[13]+line[14])
        courselist.append(line[17]+line[18]+line[19]+line[20])
        courselist.append(line[22]+line[23]+line[24]+line[25])
        courselist.append(line[28]+line[29]+line[30]+line[31])
    for line in combC:
        courselist = []
        courselist.append(line[1]+line[2]+line[3]+line[4])
        courselist.append(line[6]+line[7]+line[8]+line[9])
        courselist.append(line[11]+line[12]+line[13]+line[14])
        courselist.append(line[17]+line[18]+line[19]+line[20])
        courselist.append(line[22]+line[23]+line[24]+line[25])
        courselist.append(line[28]+line[29]+line[30]+line[31])

main()