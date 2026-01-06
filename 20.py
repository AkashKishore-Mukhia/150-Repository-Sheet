def findMagical(nums):
    sm = 0
    for num in nums:
        sm += num
    
    if perfectSquare(num):
        gcdValue = findgcd(num)
        if findPrime(gcdValue):
            return 'MAGICAL'

    return 'NOT MAGICAL'

def findPrime(num):
    if num < 2: 
        return False
    elif num == 2:
        return True
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0:
            return False
    
    return True


def perfectSquare(num):
    val = num ** 0.5
    return val == int(val)

def findgcd(nums):
    digits = []
    while nums:
        digits.append(nums % 10)
        nums //= 10
    
    value = 0
    for i in range(len(digits)):
        value = gcd(value, digits[i])
    
    return value

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


if __name__ == "__main__":
    nums = list(map(int, input('Enter the nums: ').split(',')))
    print(findMagical(nums))