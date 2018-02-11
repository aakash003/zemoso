def genPrimes():
    p = 1
    primes = []
    while True:
        p += 1
        if all(p%i for i in primes):
            primes += [p]
            yield p
