# Aplicatie Python
# Lab.  S8 - Polinoame in Python
# Todo : Suma si produsul a doua Polinoame | [!] f.readlines()
# exemplu --> d_pol = citire_date('polinom.txt')
def citirea_datelor(nume):
    grad=[]
    g=[]
    c=[]

    f=open(nume,'rt')
    linie=f.readline()
    g.append(linie)
    linie=f.readline()
    c.append(linie)
    f.close()
    for i in range(len(c)):
        c[i]=c[i].split()
    for i in range(len(g)):
        g[i]=g[i].split()
    grad=[int(x) for x in g[0]]
    coeficient=[int(x) for x in c[0]]
    for i in range(len(coeficient)):
        c1=coeficient[i]
        c2=grad[i]
        polinom[c1]=c2
    return polinom

def afisarea_polinomului(polinom,coeficient):
    print('P(x)=',end='')
    for i in coeficient:
        if polinom[i]==0:
            print(i,end='+')
        else:
            print(i,end='*')
            print('x',end='^')
            if i==coeficient[len(coeficient)-1]:
               print(polinom[i])
            else:
                print(polinom[i],end='+')
polinom={}
coeficient=[]

print("Citirea datelor din polinom : ")
print("---------------------------")
polinom=citirea_datelor('polinom.txt')
print(polinom)

print("\n\nAfisarea datelor din polinom : ")
print("---------------------------")
afisarea_polinomului(polinom,coeficient)
