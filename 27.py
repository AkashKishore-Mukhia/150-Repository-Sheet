def getFibo(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    return num * getFibo(num - 1)
        
    




if __name__ == "__main__":
    num = int(input('Enter the number: '))
    fact = getFibo(num)
    sum = 0
    while fact:
        sum += fact % 10
        fact //= 10
    
    print(sum)