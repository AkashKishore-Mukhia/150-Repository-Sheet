def checkN(num):
    divisors = {1, }

    for div in range(2, int(num ** 0.5)+1):
        if num % div == 0:
            divisors.add(div)
            divisors.add(num // div)
    
    return sum(divisors) == num




if __name__ == "__main__":
    N = int(input('Enter the number: '))
    print(checkN(N))