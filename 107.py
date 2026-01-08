def printPyramid(row):

    col = 2 * row - 1
    
    for i in range(row):
        for j in range(col//2 - i):
            print(' ', end = '')
        
        a = 64
        alphaRange = 2 * (i+1) 
        for j in range(alphaRange - 1):
            if j < (alphaRange // 2): a += 1
            else: a -= 1
            print(chr(a), end='')

        for j in range(col//2 - i):
            print(' ', end = '')
        
        print()

            





if __name__ == "__main__":
    row = int(input('Enter the number of rows: '))
    printPyramid(row)