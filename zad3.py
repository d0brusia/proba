import random
def kostka(ilosc):
    lista=[]
    for i in range(ilosc):
        i=random.randint(1,6)
        lista.append(i)
    return print(lista)

ilosc=int(input("Ile rzutów kostką?\n"))
print(kostka(ilosc)) 

print("omg nie wierze w to co sie dxirjr")
