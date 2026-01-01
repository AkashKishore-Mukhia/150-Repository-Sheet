def findPowerLevel(nums):
    largest = nums[0]
    smallest = nums[0]

    for num in nums:
        largest = max(largest, num)
        smallest = min(smallest, num)
    
    return [largest, smallest]




if __name__ == "__main__":
    nums = list(map(int, input('Enter array of numbers: ').split(',')))
    large, small = findPowerLevel(nums)
    print('Largest: {}, Smallest: {}'.format(large, small))