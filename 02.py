from math import sqrt

num = int(input())

for i in range(2, int(sqrt(num))):
    if num % i == 0:
        print('Not Prime')
        break
    else:
        print('Prime')
        break

