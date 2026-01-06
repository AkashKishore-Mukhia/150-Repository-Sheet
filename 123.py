def countSteps(N):
    steps = 0

    while N != 1:
        if N % 2:
            N = N *  3 + 1
        else:
            N //= 2
        steps += 1
    
    return steps




if __name__ == "__main__":
    N = int(input('Enter the number: '))
    print(countSteps(N))