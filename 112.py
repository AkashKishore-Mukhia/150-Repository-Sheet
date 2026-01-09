def printTriangle(N):
    num = 1
    for i in range(1, N+1):
        for j in range(i):
            print(num, end=' ')
            num += 1
        print()




if __name__ == "__main__":
    N = int(input('Enter the row number: '))
    printTriangle(N)