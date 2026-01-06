def power(b, e):
    prod = 1
    for i in range(e):
        prod *= b
    
    return prod





if __name__ == "__main__":
    b = int(input('Enter base: '))
    e = int(input('Enter exponent: '))
    print(power(b, e))