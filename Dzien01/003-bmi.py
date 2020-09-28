
# obliczanie BMI
waga = int( input("Podaj wagę w kg: ") )
wzrost = int ( input("Podaj wzrost w cm: ") )

bmi = waga / (wzrost/100)**2

#print("Twój BMI:", round(bmi, 2) )
s = f"Twoj BMI: {bmi:.0f}"
s = "Twoj BMI " + str(round(bmi,2))
print(s)