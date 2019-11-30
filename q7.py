def isPrime(num):
    if num <= 1:
        return 0
    factor = 0
    for i in range(num):
        if num % (i + 1) == 0:
            factor += 1
    if factor == 2:
        return 1
    else:
        return 0


for n in range(-2,100):
    if isPrime(n):
        print(n, 'is Prime')
    else:
        print(n, 'is NOT Prime')


