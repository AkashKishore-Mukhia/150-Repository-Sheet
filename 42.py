def printDivisors(num):
    
    for div in range(1, num+1):
        if num % div == 0:
            print(div, end=',')




if __name__ == "__main__":
    num = int(input('Enter the num: '))
    printDivisors(num)