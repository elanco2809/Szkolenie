
# Przeciążanie magic-methods

class Vector:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.__tmp = ""

    def __str__(self):
        return f"Wektor [{self._x},{self._y}]"

    def add_vector(self, other_vector):
        return Vector(self._x+other_vector._x, self._y+other_vector._y)

    def __add__(self, other_vector):
        if type(other_vector) is Vector:
            return Vector(self._x + other_vector._x, self._y + other_vector._y)
        #if type(other_vector) is int or type(other_vector) is float:
        if type(other_vector) in [int, float]:
            return Vector(self._x + other_vector, self._y + other_vector)
        if type(other_vector) is tuple:
            if len(other_vector)==2:
                for elem in other_vector:
                    if not type(elem) in [int, float]:
                        raise TypeError("element krotki nie jest z zakresu int lub float")
                return Vector(self._x + other_vector[0], self._y + other_vector[1])
            else:
                raise TypeError("mozna dodac krotke 2-elementowa")
        raise TypeError("parametr nie jest wektorem")

    def __sub__(self, other_vector):
        return Vector(self._x-other_vector._x, self._y-other_vector._y)

wektor1 = Vector(2,-2)
wektor1.__tmp = 2
wektor2 = Vector(-2,2)
print(wektor1)
print("suma=", wektor1.add_vector(wektor2))
print("suma=", wektor1+ (3.0,-3.0) )
print("roznica=", wektor1-wektor2)
