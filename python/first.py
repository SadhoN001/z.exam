def PrimeNumber(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def GenaratePrime(n):
    primes = []
    num = 2  

    while len(primes) < n:
        if PrimeNumber(num):
            primes.append(num)
        num += 1
    
    return primes

n = int(input(" numbers: "))
primes = GenaratePrime(n)
print(f"The first {n} prime numbers: {primes}")
