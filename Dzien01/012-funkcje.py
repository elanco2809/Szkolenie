#import math
from math import pi

def foo():
    return

def oblicz_pole_kola(r):
    return r**2 * pi

def oblicz_obwod_kola(r):
    return 2*pi*r

def oblicz_kolo(r):
    return oblicz_pole_kola(r), oblicz_obwod_kola(r)

print(oblicz_kolo(3))

def nowy_pracownik(imie, nazwisko, telefon="22456789", email="info@firma.pl"):
    osoba = dict()
    osoba["imie"] = imie
    osoba["nazwisko"] = nazwisko
    osoba["telefon"] = telefon
    osoba["email"] = email
    return osoba

print(nowy_pracownik("Marian","Witkowski","606111222", "marian@host.pl"))
print(nowy_pracownik("Jan","Kowalski"))
print(nowy_pracownik("Adam","Nowak", email="adam@nowak.pl"))
print(nowy_pracownik("Jan","Nowak", "606999888"))
print(nowy_pracownik("Jan","Nowak", email="jn@host.pl", telefon="501333444"))

# funkcja z dowolna liczba parametrów
def wiele_argumentow(param1, param2, *params, param_opcja="*"):
    #s = "Ala ma kota"
    #s.split(" ")
    return param_opcja.join([str(arg).upper() for arg in params])


print("="*60)
print(wiele_argumentow(1,2,3,"Test","Ala", param_opcja="_"))

# funkcja z parametrami nazwanymi
def funkcja_params(**kwargs):
    print("zawartosc kwargs=", kwargs)
    print("wiek=", kwargs["wiek"])
    print("imie=", kwargs["imie"])
    print("nazwisko=", kwargs["nazwisko"])

print("="*60)
funkcja_params(imie="Jan", nazwisko="Kowalski", wiek=22)
