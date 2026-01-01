N = int(input())


fact = 1
print('{}! = 1'.format(N), end='')
for num in range(2, N+1):
    fact = fact * num
    print(' x {}'.format(num), end='')

print('= {}'.format(fact))