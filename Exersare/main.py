# Print in Python
print("Salut din python 3.9.2 :)")
# --------------------------------- #
# Citirea si afisarea
x = input("Dati o valoare lui x ")
y = input("Dati o valoare lui y ")
print("Cele 2 valori sunt ",x,y)
#Afisarea celor 2 valori ^
print("Cele 2 valori concatenate sunt ",x+y)
#Cele 2 valori concatenate ^
x = float(x)
y = float(y)
print("X+Y=",x+y)
print("\n")
# --------------------------------- #
# If else
x=int(input("Dati o valoare lui x "))
y=int(input("Dati o valoare lui y "))
print(x+y)
if x+y>0:
    print("Suma este pozitiva")
else:
    print("Suma este negativa")
print("\n")
# --------------------------------- #
# for
N=10
v=[0]*N
for i in range(N):
    if i%2==1:
        a=0
    else:
        a=i
    v[i]=a
print(v)
print("Suma elementelor este ",sum(v))
print("\n")
# --------------------------------- #
# while
i=0
while True:
    i+=1
    c=input("Cuvantul "+str(i)+"=")
    if len(c)==0:
        break
print("\n")
# --------------------------------- #
# Matrice 
N=3
mat=[[0 for i in range(N)]for j in range(N)]
for i in range(N):
    for j in range(N):
        mat[i][j]=i+j

print("Afisarea matricii pe linii: ")
for i in range(N):
    print(mat[i])
print("Afisare matrice : ",mat)
print("\n")
# --------------------------------- #
