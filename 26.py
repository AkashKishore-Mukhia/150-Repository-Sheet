def printPattern(row):
    
    for num in range(1, row*2 + 1):
        print(num, end=' ')




if __name__ == "__main__":
    row = int(input('Enter the row number: '))
    printPattern(row)