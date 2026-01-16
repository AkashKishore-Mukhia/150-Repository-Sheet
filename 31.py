def findMedian(nums):
    N = len(nums)

    if N % 2 == 0:
        return (nums[N // 2] + nums[N // 2 - 1]) // 2
    

    return nums[N // 2]



if __name__ == "__main__":
    nums = list(map(int, input('Enter the sequence: ').split(',')))
    nums.sort()
    print(findMedian(nums))