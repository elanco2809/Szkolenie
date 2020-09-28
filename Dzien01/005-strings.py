
# Łancuchy znaków
s = " Ala ma kota i kot ma pchły "
print(s.strip()) #usuwa spacje na poczatku i koncu
print(s.upper())
print(s.lower())
print(s.strip().capitalize())
print(s.strip().title())
print(s.center(80))
print(s.replace("a","*",2))
print(s.count("ma"))
print(s.lstrip().startswith("Ala"))
print(s.rstrip().endswith("ły"))

if "kota" in s:
    print("Tak, jest 'kota' ")