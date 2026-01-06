# N = int(input())


# fact = 1
# print('{}! = 1'.format(N), end='')
# for num in range(2, N+1):
#     fact = fact * num
#     print(' x {}'.format(num), end='')

# print('= {}'.format(fact))


# recursive solution

def fact(N):
    if N == 1 or N == 0:
        return 1
    return N * fact(N-1)



if __name__ == "__main__":
    N = int(input('Enter the number: '))
    print(fact(N))