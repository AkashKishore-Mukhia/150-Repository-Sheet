def gcd(a, b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a



if __name__ == "__main__":
    print('Enter two numbers below you want GCD of: ')
    a, b = list(map(int, input('Enter Number(separate by space): ').split()))
    print(gcd(a, b))