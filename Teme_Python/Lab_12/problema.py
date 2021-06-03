# Sa da o matrice patratica de ordin n si numarul intreg m (m&lt;n). Sa se
#conceapa un algoritm care calculeaza suma elementelor fiecarei submatrici de
#ordin m.
#Exemplu:
#n=3
#A = 1 2 3
#    4 5 6
#    7 8 9
# m=2
#S=(1+2+4+5=12 2+3+5+6=16 4+5+7+8=24 5+6+8+9=28)
# 12 16 24 28
#
#
# Rezolvare problema #

def Citire_tst():
    n=int(input("Dati valoarea lui n : "))
    matrice=[0]*n
    for i in range(n):
        matrice[i]=[int(x) for x in input(f"Linia {i} ").split()]
    m=int(input("Dati valoarea lui m : "))
    if n>m:
        print("< m > are o valoarea corecta")
    else:
        print("< m > nu are o valoarea corecta. Modificati")
        m=int(input("Dati valoarea lui m : "))

def Citire_fisier(nume):
    file=open(nume,'rt')
    n=file.readline()
    matrice=[0]*n
    for i in range(n):
        matrice[i]=[int(x) for x in file.readline().split()]
    m=file.readline()

def afisare_matrice(matrice):
    for i in range(matrice):
        print(matrice[i])

def calculeaza_sume(matrice,m):
    suma=0
    for i in range(matrice):
        for j in range(matrice):
            suma+=matrice[n-i][m-j]
    suma=0
