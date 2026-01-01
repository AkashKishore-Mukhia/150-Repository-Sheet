def reverse(s):
    return s[len(s)::-1]




if __name__ == "__main__":
    s = input('Enter the message: ')
    print(reverse(s))