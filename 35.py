def getNthTriangel(n):
    return n * (n + 1) // 2




if __name__ == "__main__":
    n = int(input('Enter the n-th term: '))
    print(getNthTriangel(n))