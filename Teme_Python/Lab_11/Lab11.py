# Laborator 11 - Sudoku
# Aplicatie in Python

#---------------#
# F u n c t i i #
#---------------#

def citire_fisier(func):
    numar=func.readline()
    for i in range(9):
        for j in range(9):
            mat[i][j]=0 # init cu 0 sudoku grid
    for i in range(numar):
        v[0]=[int(x) for x in func.readline().split()]
        mat[v[0][0]-1][v[0][1]-1]=v[0][2]

def afisare_date():
    for i in range(9):
        for j in range(9):
            print(mat[i][j],"\n")
    print()

'''def posibil_line(numar,)

def rezolvare_problema():
    coordonate=[0,0]'''

def info_autor():
    print("Program realizat de Murarasu Matei - George, grupa 3111C\n")

def exit_program():
    exit(0)

#---------------------------------------#
# P r o g r a m       p r i n c i p a l #
#---------------------------------------#

mat=[0]*9
for i in range(9):
    mat[i]*=[0]*9
func=open("date.txt","rt")
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
        citire_fisier(func)
    if optiune == 'CT':
        citire_tastatura()
    if optiune == 'A':
        afisare_date()
    if optiune == 'R':
        rezolvare_problema()
    if optiune == 'I':
        info_autor()
    if optiune == 'X':
        exit_program()
