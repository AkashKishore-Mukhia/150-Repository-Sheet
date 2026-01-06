def squareSum(num):
    sm = 0

    while num:
        sm += (num % 10) ** 2
        num //= 10
    return sm




if __name__ == "__main__":
    num = int(input('Enter the number: '))
    print(squareSum(num)) 
