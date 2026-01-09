def printPascalTriangle(N):
    triangle = []
    idx = 0
    for i in range(N):
        for j in range(i):
            if j == 0:
                triangle.append(1)
            else:
                triangle.append(triangle[idx-(i+1)] + triangle[idx-i])
            print(triangle[idx], end=' ')
            idx += 1
            
        triangle.append(1)
        print(triangle[idx], end=' ')
        print()
        idx += 1

    print(triangle)




if __name__ == "__main__":
    N = int(input('Enter the row number: '))
    printPascalTriangle(N)