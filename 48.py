def FindSecondLargest(nums):
    mx = 0
    smx = 0

    for num in nums:
        if num > mx:
            smx = mx
            mx = num
        elif num > smx and num < mx:
            smx = num
        
    return smx



if __name__ == "__main__":
    nums = list(map(int, input('Enter the numbers: ').split(',')))
    print(FindSecondLargest(nums))