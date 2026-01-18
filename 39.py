def findLastDigitSum(n):
    if n <= 9:
        return n

    sm = 0
    while n:
        sm += n % 10
        n //= 10
    
    return findLastDigitSum(sm)



if __name__ == "__main__":
    n = int(input('Enter the number: '))
    print(findLastDigitSum(n))