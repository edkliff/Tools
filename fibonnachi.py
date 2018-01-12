import time

def fib(n):
    if n in (0, 1):
        return 1
    else:
        return fib(n-1) + fib(n-2)


for z in range(1, 40):
    s = time.time()
    print('Element ({}) = '.format(z), fib(z))

    e = time.time() - s
    print(e)
