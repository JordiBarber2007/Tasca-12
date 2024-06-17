import random

def Gllistaaleatoris():
    l=[]
    for i in range(3):
        l.append(random.randint(1,9))
    return l
def llegir_llista():
    l=[]
    for i in range(3):
        l.append(int(input("Introdueix el numero: ")))
    return l

def comparar(l,m):
    a = [0,0,0]
    for i in range(3):
        if l[i]==m[i]:
            a[i]=10
    if a [0]==10 and a[1]==10 and a[2]==10:
        print("Enhorabona ho has encertat tot! ")
        return 0
    for i in range(3):
        if a[i]==10:
            print("L'element {} es correcte".format(m[i]))
        elif a [i]==5:
            print("L'element {} existeix pero no esta al seu lloc".format(m[i]))
        else:
            print("L'element {} no existeix".format(m[i]))

def pex1():
    op=1
    l=Gllistaaleatoris()
    while op!=0:
        m = llegir_llista()
        op = comparar(l,m)
