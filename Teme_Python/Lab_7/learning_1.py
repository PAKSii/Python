# Aplicatie Python
# Lab.  S7 - Functii, meniuri si dictionare in Python
# TODO : Optiunea 6 medii nu functioneaza
def optiune():
    opt=int(input('opt='))
    return opt
def informatii_std():
    info=0
    global lst
    f=open('studentii.txt','rt')
    while True:
        linie=f.readline()
        if len(linie)==0:
            break
        lst.append(linie)
        info=1
    f.close()
    for i in range(len(lst)):
        lst[i]=lst[i].split(',') # Separarea listelor de operatorul ","
    '''for i in range(len(lst)): # Afisarea elementelor din liste
        print(lst[i])'''
    if info==1:
        print("Datele din fisierul <studentii.txt> au fost citite cu succes!")
    else:
        print("Datele din fisier nu au fost citite cu succes.")


def afis_studenti(lst): # Optiune meniu 2
    print("Se afiseaza Studentii:\n")
    print('ID \t\t NUME STUDENT')
    print('-------------------------')
    for i in range(len(lst)):
        print(lst[i][0],end='')
        print("\t\t",lst[i][1])

def afisez_std(lst): # Optiune meniu 3
    print("Se afiseaza Notele:\n")
    print('ID \t\t NOTE')
    print('-------------------------')
    for i in range(len(lst)):
        print(lst[i][0],end='')
        print("\t\t",lst[i][2],end='')

def afis_studenti_note(lst): # Optiune meniu 4
    print("Se afiseaza informatiile din fisier\n")
    print('ID \t\t Nume Student \t\t Note')
    print('------------------------------------------------')
    for i in range(len(lst)):
        print(lst[i][0],end='')
        print("\t\t",lst[i][1],end='')
        print("\t\t",lst[i][2],end='')

def cautare_nume(lst): # Optiune meniu 5
    gasit=0
    nume=input("Dati numele studentului: ")
    for i in range(len(lst)):
        if lst[i][1]==nume:
            print('ID \t\t Nume Student \t\t Note')
            print('------------------------------------------------')
            gasit=1
            print(lst[i][0],end='')
            print("\t\t",lst[i][1],end='')
            print("\t\t",lst[i][2],end='')
    if gasit==0:
        print(f"Studentul cu numele <{nume}> nu exista in lista.\n")
def studenti_promovati(list): # Optiune meniu 6
    media=[]
    for i in range(len(lst)):
        note=[int(x) for x in lst[i][2].split(" ")]
        med=(note[0]+note[1]+note[2])/3
        note.clear()
        media.append(med)
    media_rot=[round(x,2) for x in media]
<<<<<<< HEAD
    print("Se afiseaza studentii promovati: \n")
=======
>>>>>>> da1541eeb33598f912b643f8eb3ffd555d628790
    print('ID \t\t Nume Student \t\t Media')
    print('------------------------------------------------')
    for i in range(len(lst)):
        print(lst[i][0],end='')
        print("\t\t",lst[i][1],end='')
        print("\t\t",media_rot[i])

def info_autor(): # Optiune meniu 7
    print("Program realizat de Murarasu Matei - George, grupa 3111C")

def end_program(): # Optiune meniu 8
    exit(0)

#Inceperea programului principal
print("\t\t\tM E N I U")
menu={
1:'1 - Incarcati informatii despre studenti din fisier',
2:'2 - Afisare studenti',
3:'3 - Afisare note',
4:'4 - Afisare studenti si notele obtinute',
5:'5 - Cautare student dupa nume',
6:'6 - Afisare studenti promovati',
7:'7 - Info autor',
8:'8 - Terminare program'}
lst=[]
while True:
    print(menu[1])
    print(menu[2])
    print(menu[3])
    print(menu[4])
    print(menu[5])
    print(menu[6])
    print(menu[7])
    print(menu[8])
    print("Introduceti optiunea: ")
    opt=int(input('opt='))
    if opt==1:
        informatii_std()
        print("\nSelectati urmatoarea optiune: ")
        opt=int(input('opt='))
    if opt==2:
        afis_studenti(lst)
        print("\nSelectati urmatoarea optiune: ")
        opt=int(input('opt='))
    if opt==3:
        afisez_std(lst)
        print("\nSelectati urmatoarea optiune: ")
        opt=int(input('opt='))
    if opt==4:
        afis_studenti_note(lst)
        print("\nSelectati urmatoarea optiune: ")
        opt=int(input('opt='))
    if opt==5:
        cautare_nume(lst)
        print("\nSelectati urmatoarea optiune: ")
        opt=int(input('opt='))
    if opt==6:
        studenti_promovati(lst)
        print("\nSelectati urmatoarea optiune: ")
        opt=int(input('opt='))
    if opt==7:
        info_autor()
        print("\nSelectati urmatoarea optiune: ")
        opt=int(input('opt='))
    if opt==8:
        end_program()
