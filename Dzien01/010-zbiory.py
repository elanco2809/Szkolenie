
zbior1 = set() #pust zbior
zbior1 = { 1, 2, True, 0, False, None }

lista = [1,2,3,1,2,3]
print(list(set(lista)))

zbior1.add("A")
zbior1.pop()
zbior1.add(1)

for x in zbior1:
    print(x)

zbiorA = set()
for x in range(1,11):
    zbiorA.add(x)

zbiorB = set()
for x in range(8,16):
    zbiorB.add(x)

print("A=",zbiorA)
print("B=",zbiorB)
print("Unia:", zbiorA.union(zbiorB))
print("Czesc wsp.:", zbiorA.intersection(zbiorB))
print("Roznica symetryczna:", zbiorA.symmetric_difference(zbiorB))
print("A - B", zbiorA.difference(zbiorB))