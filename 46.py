def printPyramid(row):
    for r in range(1, row+1):
        for c in range(1, r+1):
            print(c, end='')
        print()




if __name__ == "__main__":
    row = int(input('Enter number of rows: '))
    printPyramid(row)