import math


def checkNarcissistic(n):
    tmp = n
    sum = 0
    digits = math.floor(math.log10(abs(n))) + 1
    while tmp:
        sum += (tmp %10) ** digits
        tmp //= 10

    return n == sum



if __name__ == "__main__":
    N = int(input('Enter a Number: '))
    print(checkNarcissistic(N))