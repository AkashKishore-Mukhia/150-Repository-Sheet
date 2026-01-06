def checkHappy(N, num):
    if N == 1:
        return True
    
    sm = 0
    while N:
        sm += (N % 10) ** 2
        N //= 10

    if num == sm:
        return False
    
    return checkHappy(sm, num)




if __name__ == "__main__":
    N = int(input('Enter the number: '))
    print(checkHappy(N, N))