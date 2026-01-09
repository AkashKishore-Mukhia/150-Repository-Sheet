def printChessBoard(row):
    boxCol = 1
    boxRow = 1
    for i in range(row):
        for j in range(row):
            print(boxCol, end=' ')
            boxCol ^= 1
        
        boxRow ^= 1
        boxCol = boxRow
        print()





if __name__ == "__main__":
    row = int(input('Etner number of rows: '))
    printChessBoard(row)