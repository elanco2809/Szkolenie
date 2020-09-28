from functools import reduce

# Map, Filter, Reduce

imiona = ["Anna", "Waldemar", "Piotr", "Andrzej", "Agata", "Olaf"]

result = [i for i in imiona if i[0]=="A" ]
print(result)

def start_a(s):
    return s[0]=="A"

#print(list(filter(start_a, imiona)))
print(list(filter(lambda s: s[0]=="A" , imiona)))

# mapowanie elementow listy
print( list( map(lambda s:len(s), imiona) ) )

# reduce
lista = [2,3,5,8,10]

def mul(x, y):
    return x*y

print(reduce(lambda x,y: x*y, lista ))