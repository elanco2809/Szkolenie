
with open("plik-zapis.txt", "wt") as fd:
    fd.write("To jest 1 linia pliku txt\n")
    fd.write("To jest 2 linia\n")
    fd.writelines(["Kolejna linia 1\n", "Kolejna linia 2\n"])


# windows - c:\tmp\plik.txt
s = "c:\\tmp\\plik.txt"
s = "c:/tmp/plik.txt"
s = r"c:\tmp\plik.txt"

bytes = bytearray()
for i in range(48,59):
    bytes.append(i)

with open("plik.bin", "wb") as fd:
    fd.write(bytes)