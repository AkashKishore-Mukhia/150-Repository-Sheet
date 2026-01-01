def findFibonacci(N):
    firstFibo = 0
    secondFibo = 1
    if N == 1 or N == 0:
        return firstFibo
    if N == 2:
        return secondFibo
    
    for _ in range(N-1):
        firstFibo, secondFibo = secondFibo, firstFibo + secondFibo
        
    return secondFibo
        

if __name__ == "__main__":
    N = int(input())
    print(findFibonacci(N))
