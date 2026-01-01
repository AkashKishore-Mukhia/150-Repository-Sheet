a, b = list(map(int, input().split()))

lcm = 1
while lcm % a or lcm % b:
    lcm += 1

print(lcm)
