# Laborator 10 - Backtracking
# Aplicatie in Python

#---------------#
# F u n c t i i #
#---------------#
global poduri,ok
def citire_fisier():
    global numar,ins_start
    f=open('date.txt','rt')
    line=f.readline()
    numar=int(line)
    line=f.readline
    ins_start=line
    insule=[]
    while True:
        line=f.readline()
        if len(line)==0:
            break
        insule=[int(x) for x in line.split()]
        poduri.append(insule)
        ok=1
    if ok==0:
        print("Datele din fisier nu au fost citite cu succes.\n")
    else:
        print("Datele din fisier au fost citite cu succes.\n")

def citire_tastatura():
    global numar,ins_start
    numar=int(input('Introduceti numarul de poduri:  '))
    ins_start=int(input('Tastati insula de la care doriti sa incepeti:  '))
    global poduri
    poduri=[]
    for i in range(numar):
        insule=[int(x) for x in input('Podul cu numarul '+str(i)+' uneste insulele:').split()]
        poduri.append(insule)

def afisare():
    if numar==0:
        print("Vectorii nu au nicio data introdusa\n")
    else:
        for i in range(numar):
            print(poduri[i])
    print()


def Plimbare(insula_crt,k):
    global x,poduri,n
    if n==k:
        print(x)
    else:
        for i in range(n):
            if POSIBIL(i,k,insula_crt):
                x[k]=i
                if insula_crt==pod[i][0]:
                    insule=poduri[i][1]
                else:
                    insule=poduri[i][0]
                Plimbare(insule,k+1)
    print()


def POSIBIL(i,k,insula_crt):
    global x,poduri,ins_start
    for j in range(k):
        if x[j]==i:
            return False
    return poduri[i][0]==insula_crt or poduri[i][1]==insula_crt

def info_autor():
    print("Program realizat de Murarasu Matei - George, Grupa 3111C\n")

def end_program():
    exit(0)
#---------------------------------------#
# P r o g r a m       p r i n c i p a l #
#---------------------------------------#
poduri=[]
numar=0
ok=0
x=[]
n=0
print("\t\t\tM E N I U")
meniu={
'CF':'CF - Citire date din fișier : ',
'CT':'CT - Citire date de la tastatura : ',
'A':'A - Afisarea datelor',
'R':'R - Rezolvarea problemei',
'I':'I - Info autor',
'X':'X - Terminare program'}

while True:
    print(meniu['CF'])
    print(meniu['CT'])
    print(meniu['A'])
    print(meniu['R'])
    print(meniu['I'])
    print(meniu['X'])
    print("Introduceti optiunea : ")
    optiune=input("Optiune = ")
    print()
    if optiune == 'CF':
        citire_fisier()
    if optiune == 'CT':
        citire_tastatura()
    if optiune == 'A':
        afisare()
    if optiune == 'R':
        x=[0]*n
        Plimbare(ins_start,0)
    if optiune == 'I':
        info_autor()
    if optiune == 'X':
        end_program()
