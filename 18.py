def printTable(N):
    for i in range(1, 6):
        print('{} x {} = {}'.format(N, i, N * i), end=' ')
    




if __name__ == "__main__":
    N = int(input('Enter the number of which multiplication table you want: '))
    printTable(N)