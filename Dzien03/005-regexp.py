import re

"""
k...a - 5 znakow , zaczyna od "k" a konczy na "a
Ma.*k - zaczyna się od "Ma" i kończy na "k" z dowolną liczbą znaków pomiędzy
Ma.+k - zaczyna się od "Ma" i kończy na "k" z  liczbą znaków pomiędzy >0
Ma?k - zaczyna się od "Ma" i kończy na "k" z  liczbą znaków pomiędzy 0 lub 1
[0-9]{2}-[0-9]{3} - maska dla kodu pocztowego

^[0-9]{2}-[0-9]{3}$ - dokł. zaczyna się i konczy na

[^0-9A-Za-z]{3,} - przynajmniej 3 znaki spoza zakresu 0-9, A-Z, a-z

[0-9] eq \d
\D - nie cyfry
\s - znaki białe
\S - inne niż znaki białe
\w - [0-9A-Za-z_]
\W - inne niż [0-9A-Za-z_]

"""

txt = "Mały Marek machał makatką trzymając trzy piwa"
result = re.findall("ma[a-z]{0,}k", txt.lower())
print(result)

zip_code = "02-999"
result = re.match("^[0-9]{2}-[0-9]{3}$", zip_code)
print(result)

cre = re.compile("\d")
result = cre.findall("Kwota do zapłaty to 1234,56PLN , termin platnosci 7 dni. Wygenerowano 13:33")
print(result)

cre = re.compile("\d+")
result = cre.findall("Kwota do zapłaty to 1234,56PLN , termin platnosci 7 dni. Wygenerowano 13:33")
print(result)

txt = "   Mały \r\nMarek\tmachał \f makatką trzymając trzy piwa   "
#s = txt.replace(" ","").replace("\r","").replace("\n","")
txt = re.sub("\s", "*", txt, 3)
print(txt)

txt = "Znaleziono: 120 rekordów."
cre = re.compile("\d+")
result = cre.findall(txt)
print(result)

result = "".join([ch for ch in txt if ch.isdigit()])
print(result)