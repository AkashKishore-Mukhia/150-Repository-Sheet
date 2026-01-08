# Sieve of Eratosthenes
# Marking multiples of each prime as non-prime


def primes(nums):
    prime_flag = [True for i in range(nums[-1])]
    prime_flag[0] = False
    prime_flag[1] = False

    p = 2

    while p*p <= nums[-1]:
        
        if prime_flag[p]:
            # starting from p*p since smaller mutiples have already been marked by smaller primes
            for i in range(p*p, nums[-1], p):
                prime_flag[i] = False
        
        p += 1
    

    for i in range(nums[0], nums[-1]):
        if prime_flag[i]:
            print(i, end=' ')
                

    




if __name__ == "__main__":
    nums = list(map(int, input('Enter the numbers: ').split()))
    primes(nums)