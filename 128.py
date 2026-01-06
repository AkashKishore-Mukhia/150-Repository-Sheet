def checkAmstrongNumber(N):
    cnt = getDigitCount(N)
    tmp = N
    sm = 0
    while tmp:
        sm += (tmp % 10) ** cnt
        tmp //= 10
    
    return sm == N


def getDigitCount(N):
    cnt = 0
    while N:
        N //= 10
        cnt += 1
    return cnt


if __name__ == "__main__":
    N = int(input('Enter the Number: '))
    print(checkAmstrongNumber(N))
