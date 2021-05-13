# Laborator_9 - Python
# Metoda Greedy
# Problema rucsacului
#TODO : sortare + algoritm

global pret
global volum
global obiecte
obiecte=[]
#-----------#
# metoda cu liste de liste
def citire_elemente():
    Volum=int(input("Specificati volumul rucsacului : "))
    numar=int(input("Specificati numarul de elemente "))
    for i in range(numar):
        print(f"Produsul cu numarul {i+1}")
        pret=int(input("pret = "))
        volum=int(input("Volum = "))
        obiecte.append([pret,volum,pret/volum])

def afisare():
    print(obiecte)
'''i=1
vt=pt=0
while (vt<V and i<=n)
 if vt+v[i]<=V:
     x[i]=1
     pt=pt+p[i]
     vt=vt+v[k]
     else:
         x[i]=(V-vt)/v[i]
         vt=V
         pt=pt+p[i]x[i]
    i=i+1
    print("Pretul total al obiectelor din rucsac= ",pt,"Volumul ocupat= ",vt)
    print("In rucsac s-au introdus:")
    for i in range(n)
        if x[i]>0:
            print("obiectul",i,"(",v[i]x[i],","p[i]")")'''

citire_elemente()
afisare()
