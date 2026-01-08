def checkPerfectSquare(N):
    return pow(N, 0.5) == int(pow(N, 0.5))


if __name__ == "__main__":
    N = int(input('Enter the number: '))
    print(checkPerfectSquare(N))