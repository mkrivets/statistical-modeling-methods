import math as m


def isPrime(n):
    if (n == 1):
        return False
    prime = True
    i = 2
    while (i <= round(m.sqrt(n))):
        if (n % i == 0):
            prime = False
            break
        i += 1
    return prime


def twoPrimes(min):
    n = min + 2
    while True:
        if (isPrime(n - 1) and (isPrime(n + 1))):
            return n - 1, n + 1
        n += 1


def getMersenne(min):
    n = 0
    m = 0
    while (m <= min):
        n += 1
        m = (2 ** n) - 1
    return m


print(twoPrimes(10 ** 6))
print(twoPrimes(10 ** 9))
print(twoPrimes(10 ** 10))
print('\n')
print(getMersenne(10 ** 6))
print(getMersenne(10 ** 9))
print(getMersenne(10 ** 10))
