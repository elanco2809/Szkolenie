
# słowniki (dictionary)

osoba = dict()
osoba = {
    "imie" : "Jan",
    "nazwisko" : "Kowalski",
    "wiek" : 44,
    "dostep" : [101, 111, 131]
}

# pobieranie
print(osoba)
print(osoba["imie"])
print(osoba.get("imie1", "NoName"))

# ustawianie
osoba["wiek"] = 45
osoba.update({ "imie":"Pankracy", "wiek":60 })
print(osoba)

# usuwanie klucza
#osoba.pop("dostep")
del(osoba["dostep"])
print(osoba)

print("klucze:", osoba.keys())
print("wartosci:", osoba.values())
print("="*60)
for elem in osoba.items():
    print(elem)