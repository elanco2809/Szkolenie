
# Pętla for - iteracja

"""
for x in range(1,11):
    print(x**2)
"""

lista = ["A","AB","ABC","QWE","DD","AA"]
s = "Ala ma konta"
for index, value in enumerate(lista, 100):
    print(index,"-", value)

a, b = 10, 20
b, a = a, b
a = 10; b =20;