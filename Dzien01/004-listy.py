
# działania na listach

lista = list() # pusta lista
lista = [] # to tez lista pusta
lista = [1, True, "Ala ma kota", (200,"OK"), ['A',"B","C"] ]

print(len(lista))

lista[1] = False
x = lista[1]

lista.append(None) # dołaczanie na koniec
lista.extend([-10,-20,-30]) # dołączanie innej listy na koniec
lista.insert(0, "START")

x = lista.pop(1) # zdejmuje wartosc z listy z podanego indeksu
x = lista.index("Ala ma kota") # poszukiwanie elementu o wartości
#lista.sort() - dostępne dla list homogenicznych

print(lista)
lista.reverse()
print(lista)

lista2 = lista # kopiowanie wskaznika
lista3 = lista.copy()
lista[0] = "ABCDEF"

print(lista3)

s = "Ala ma kota i kot ma pchły"
print(s)
print(s[:4]) # pierwsze 4 znaki
print(s[-4:]) # ostatnie 4 znaki
print(s[4:6]) # tylko pierwsze "ma"
print(s[::-1]) # odwróc łancuch znaków
