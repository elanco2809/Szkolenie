
# Pętla while
i =10
while i>0:
    print(i)
    if i==5:
        break
    i -= 1 # i = i - 1

while True:
    x = int(input("Podaj liczbę >100 i podzielną przez 2: "))
    if x>100 and x%2==0:
        break

print("poza while")