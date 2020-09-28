import math

x = 10
y = 3

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y) # dzielenie całkowite
print(x%y) # dzielenie z resztą

print(x**y)
print(pow(x,y))
print(math.pow(x,y))

result = math.pow(x,y)
result = int(result)
result = str(result)
result = float(result)
print(type(result))

print("ABC" + str(2)) # konwersja do string wartości int
