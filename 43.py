def findAvg(nums):
    sum = 0
    for num in nums:
        sum += num

    return sum // len(nums)




if __name__ == "__main__":
    nums = list(map(int, input('Enter the number sequence: ').split(',')))
    print(findAvg(nums))