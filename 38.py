def printGrid(num):

    for n in range(1, num * num + 1):
        print(n, end=' ')
    print()



if __name__ == "__main__":
    num = int(input('Enter the number: '))
    printGrid(num)