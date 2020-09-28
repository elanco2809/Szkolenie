
#obsluga odczytu plikow tekstowych

fd = None
try:
    fd = open("pkn.csv", "rt")
    rows = fd.readlines()[1:]
    for row in rows:
        item = row.strip().split(",")
        if float(item[4])>=91:
            print(row, end="")
    #print(rows)
except Exception as exc:
    print(exc)
finally:
    if fd:
        fd.close()


print("="*100)
# context manager
with open("pkn.csv", "rt") as fd:
    for index, line in enumerate(fd):
        if index==0:
            continue
        print(line.strip())

print(fd.closed)
