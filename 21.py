def getSum(nums):
    sum = 0
    for num in range(nums[0], nums[-1]+1):
        if num % 2:
            sum += num

    return sum





if __name__ == "__main__":
    nums = list(map(int, input('Enter the range of values: ').split(',')))
    print(getSum(nums))