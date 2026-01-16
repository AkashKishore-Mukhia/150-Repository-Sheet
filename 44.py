def findMostFreq(nums):
    mp = {}

    for num in nums:
        if num not in mp:
            mp[num] = 1
        else:
            mp[num] += 1
    
    mx, freq = 0, 0
    for key, value in mp.items():
        if value > freq:
            freq = value
            mx = key
    
    return mx



if __name__ == "__main__":
    nums = list(map(int, input('Enter the number: ').split(',')))
    print(findMostFreq(nums))