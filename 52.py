# If we subtract a smaller number from a larger one (we reduce a larger number), GCD doesn't change.
# So if we keep subtracting repeatedly the larger of two, we end up with GCD.


def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a%b)




if __name__ == "__main__":
    a, b = list(map(int, input('Enter two numbers: ').split()))
    print(gcd(a, b))