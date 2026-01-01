def sort(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]





if __name__ == "__main__":
    nums = list(map(int, input('Enter the numbers separated by comma: ').split(',')))
    sort(nums)
    print(nums)