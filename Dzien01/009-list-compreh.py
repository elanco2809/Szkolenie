
# wyrazenia listotworcze

result = list()
for x in range(1,101):
    if x%3==0:
        result.append(x**2)

result = [x**2 for x in range(1,101) if x%3==0]
print(result)