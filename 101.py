def printPyramid(N):
    
    col = 2 * N - 1

    for i in range(N):
        for j in range(col // 2 - i):
            print(' ', end='')

        digit = 1
        value = 2 * (i+1) - 1
        for j in range(value):
            print(digit, end='')
            if j < value // 2:
                digit += 1
            else:
                digit -= 1
            
        for j in range(col // 2 - i):
            print(' ', end='')

        print()


if __name__ == "__main__":
    N = int(input('Enter row number: '))
    printPyramid(N)