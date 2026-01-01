def sum(nums):
    sum = 0
    for num in nums:
        sum += num
    
    return sum




if __name__ == "__main__":
    s = input('Enter the numbers separated by comma: ')
    if s == '':
        exit(0)
    nums = list(map(int, s.split(',')))
    print(sum(nums))