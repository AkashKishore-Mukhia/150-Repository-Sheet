def checkHarshadNumber(num):
    sm = 0
    tmp = num

    while tmp:
        sm += (tmp % 10)
        tmp //= 10
    
    return num % sm == 0




if __name__ == "__main__":
    N = int(input('Enter the number: '))
    print(checkHarshadNumber(N))