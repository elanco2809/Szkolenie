
# Generator liczb pseudolosowych
import random
import time
import uuid
import os
import binascii
import string
import hashlib

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

random.seed(time.time())
print("liczba pseudolosowa=", random.random())
print("losowanie z zakresu=", random.randint(-10, 10))
print("losowanie z zakresu z krokiem=", random.randrange(-10, 11, 2))
print("liczba losowa na podst. rozkl. Gaussa", random.gauss(10, 2))

lista = [x for x in range(10,101,10)]
print(lista)
print("losowanie z listy=", random.choices(lista, k=4)) # wylosowane zostaną 4 elementy
print("losowanie z listy=", random.sample(lista, k=4)) # wylosowane zostaną 4 elementy bez powtorzen

def pass_gen(n):
    #s = "ABCDEFGHIJKLgdf$^$%^$%@$MNOPQRSTUVdfsdfsdfswwerwer52534523523452gdf@$@!@((&a"
    s = string.printable.replace(" ","").strip()
    result = ""
    for _ in range(n):
        index = random.randint(0, len(s)-1)
        result += s[index]
    return result

for _ in range(5):
    print("haslo=", pass_gen(10))

# generowanie GUIDow
for _ in range(5):
    print("UUID4=", uuid.uuid4())
    print("UUID5=", uuid.uuid5(uuid.NAMESPACE_X500, pass_gen(20)))
    print()

# pseudolosowosc w module OS
secret = os.urandom(32)
print(secret)
print("".join([f"{x:02x}" for x in secret]))
print(binascii.hexlify(secret).decode())

print(hashlib.algorithms_available)
h = hashlib.new("sha512")
h.update("Ala ma kota".encode())
print(h.hexdigest())

gaus_data = [random.gauss(10, 2) for _ in range(50_000)]
plt.hist(gaus_data, bins=30)
plt.show()