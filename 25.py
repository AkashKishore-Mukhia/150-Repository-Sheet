def isNarcissisticNumber(num):
    count = getDigitCount(num)
    sum = 0
    tmp = num
    while tmp:
        digit = tmp % 10
        sum += pow(digit, count)
        tmp //= 10
    
    return sum == num



def getDigitCount(num):
    count = 0
    while num:
        num //= 10
        count += 1
    return count



if __name__ == "__main__":
    num = int(input('Enter the number: '))
    if isNarcissisticNumber(num):
        print('Narcissistic Number')
    else:
        print('Not a Narcissistic Number')