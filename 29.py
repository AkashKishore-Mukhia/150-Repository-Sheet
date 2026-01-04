def findMissing(nums):
    mx = 0
    missing = []
    for num in nums:
        mx = max(mx, num)

    for num in range(1, mx):
        if num in nums:
            continue
        else:
            missing.append(num)
    
    return missing





if __name__ == "__main__":
    nums = list(map(int, input('Enter the numbers: ').split(',')))
    print(findMissing(nums))