def findPalin(s):
    res = ''
    sub = ''
    for i in range(0, len(s)):
        for j in range(i, len(s)):
            sub += s[j]
            if palindrome(sub):
                if len(sub) > len(res):
                    res = sub
        sub = ''
    
    return res

def palindrome(s):
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    s = input('Enter the string: ')
    print(findPalin(s))
    