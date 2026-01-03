def printPrimes(N):
    primes = []
    for num in range(2, N):
        if num == 2:
            primes.append(num)
            continue

        for div in range(2, (num//2) + 1):
            if num % div == 0:
                break
        else:
            primes.append(num)
    return primes



if __name__ == "__main__":
    N = int(input('Enter the number: '))
    print(printPrimes(N))