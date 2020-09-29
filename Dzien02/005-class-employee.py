"""

    Klasa Pracownik rejestruje ile czasu pracował i oblicza naleznosc
    Jesli pracował do 8h, to rozliczany jest wg. stawki godzinowej
    Jesli przepracował więcej niż 8h, to pierwsze 8h zaliczane jest wg. normalnej stawki
    a reszta godzin wg. 150% stawki godzinowej

"""

class Employee:
    def __init__(self, fname, lname, rate):
        self._fname = fname
        self._lname = lname
        self._rate = rate
        self._total = 0.0

    def register_time(self, hours):
        if hours<=8:
            self._total += hours*self._rate
        else:
            self._total += 8*self._rate
            self._total += (hours-8)*1.5*self._rate

    def pay_salary(self):
        print(f"Wyplata = {self._total}")
        self._total = 0.0

mirek = Employee("Mirek","Kowalski",100)
mirek.register_time(10)
mirek.register_time(7)
mirek.pay_salary()

mirek._total = 1_000_000
mirek.pay_salary()