def sumPrimes(start, end):
    primes = [True for _ in range(end+1)]
    primes[0] = False
    primes[1] = False

    p = 2

    while p*p < end+1:
        
        if primes[p]:
            for i in range(p*p, end+1, p):
                primes[i] = False
        
        p += 1
    
    sm = 0
    
    for i in range(start, end+1):
        if primes[i]:
            sm += i

    return sm





if __name__ == "__main__":
    start, end = list(map(int, input('Enter the numbers: ').split(',')))
    print(sumPrimes(start, end))