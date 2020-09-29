import time
import functools

@functools.lru_cache(128)
def fibo_rek(n):
    if n<=1:
        return n
    else:
        return fibo_rek(n-1) + fibo_rek(n-2)

def fibo_loop(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

t1 = time.time()
for _ in range(1000):
    fibo_rek(20)
t2 = time.time()
print(f"{t2-t1}")


t1 = time.time()
for _ in range(1000):
    fibo_loop(20)
t2 = time.time()
print(f"{t2-t1}")

#print(fibo_rek(20))
#print(fibo_loop(20))