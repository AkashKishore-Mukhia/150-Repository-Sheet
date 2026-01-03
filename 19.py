def getPrime(nums):
    primes = []
    for i in range(nums[0], nums[-1]+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)

    return primes



if __name__ == "__main__":
    nums = list(map(int, input('Enter the numbers separated by comma: ').split(',')))
    print(getPrime(nums))