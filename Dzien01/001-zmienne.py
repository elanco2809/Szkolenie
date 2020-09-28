
# komentarz
# komentarz linia 2

"""

    To jest komentarz
    linia 2
    linia 3
 """

x = 12
x = 12.34
x = "Ala ma \" kota"
x = 'Ala ma " kota'
x = "Ala ma ' kota"
x = None # wartość pusta

# krotka / tuple
krotka = (200, "OK")
krotka = (200,) # krotka jednoelementowa
krotka = (200, "OK", ("Response", "OK") )

#pierwszy element krotki
kod = krotka[0]
komunikat = krotka[1] # 2-gi
info = krotka[2] # trzeci

# wersja altern. (unpacking)
kod, komunikat, info = krotka
print(kod, komunikat, info, sep="|" )

#krotka[0] = 301 - krotka jest niemutowalna
#print(krotka[0])

