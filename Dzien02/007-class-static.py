from math import pi
# klasa statyczna

class Planimetria:

    @staticmethod
    def oblicz_pole_kola(r):
        return pi*r**2

wynik = Planimetria.oblicz_pole_kola(3)
print(wynik)
