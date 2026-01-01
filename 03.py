num = int(input('Enter the year:'))

if num % 400 == 0:
    print('{} is a leap year'.format(num))
elif num % 4 == 0 and num % 100:
    print('{} is a leap year'.format(num))
else:
    print('{} is not a leap year'.format(num))