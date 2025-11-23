def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 200
f200 = None
for i, val in enumerate(fib(n), start=1):
    if i == 200:
        f200 = val

print("200-е число Фибоначчи:", f200)
