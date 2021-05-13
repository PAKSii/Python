# Laborator 9 - Metoda Greedy
# Aplicatie in Python

#-----------------------#
# Functii #
global n
Si=[]
Fi=[]
def citire_fisier():
    ct=0
    with open("file.txt",'rt') as file:
        while True:
            line=file.readline()
            if len(line)==0:
                break
            Si.append(line)
            Fi.append(line)
            ct=ct+1
        print("\n")

def citire_tastatura():
    n=int(input("Cate evenimente sunt?\n"))
    for i in range(n):
        ora_i=input(f"Dati ora de inceput al evenimentului <{i+1}> : ")
        Si.append(ora_i)
        ora_f=input(f"dati ora de final al evenimentului <{i+1}> : ")
        Fi.append(ora_f)
        ora_i=ora_f=0
    print("\n")

def afisare_date():
    if len(Si)==len(Fi)==0:
        print("Liste Vide")
    else:
        print(Si)
        print(Fi)
    print("\n")

def afisare_date_sortate():
    Si.sort()
    Fi.sort()
    afisare_date()

def rezolvare():
    print(" ee")
    print("\n")

def info_autor():
    print("Program realizat de Murarasu Matei - George, grupa 3111C")
    print("\n")

def end_program():
    exit(0)


#-----------------------#
# Program principal #
#-----------------------#
pod=[]
n=0
print("\t\t\tM E N I U")
meniu={
'CF':'CF - Citire date din fișier : ',
'CT':'CT - Citire date de la tastatura : ',
'A':'A - Afisarea datelor',
'AS':'AS - Afisarea datelor sortate',
'R':'R - Rezolvarea problemei',
'I':'I - Info autor',
'X':'X - Terminare program'}
#-----------------------#
# Meniu #
while True:
    print(meniu['CF'])
    print(meniu['CT'])
    print(meniu['A'])
    print(meniu['AS'])
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
        afisare_date()
    if optiune == 'AS':
        afisare_date_sortate()
    if optiune == 'R':
        rezolvare()
    if optiune == 'I':
        info_autor()
    if optiune == 'X':
        end_program()
