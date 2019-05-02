def fibo():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a+b

for index, number in enumerate(fibo()):
    if len(str(number)) == 1000:
        print(index)
        break