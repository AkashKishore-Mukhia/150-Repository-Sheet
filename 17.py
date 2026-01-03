def findArmstrong(nums):
    resultList = []
    for i in range(nums[0], nums[-1]+1):
        sum = 0
        num = i
        while num:
            sum += pow((num % 10), 3)
            num //= 10
        
        if sum == i:
            resultList.append(sum)
    
    return resultList




if __name__ == "__main__":
    nums = list(map(int, input('Enter the range of values separated by comma: ').split(',')))
    print(findArmstrong(nums))