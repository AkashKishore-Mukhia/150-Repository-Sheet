def countDigits(num):
    count = 0
    while num:
        num //= 10
        count += 1
    
    return count




if __name__ == "__main__":
    num = int(input('Enter the number: '))
    print(countDigits(num))