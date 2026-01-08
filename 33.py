def checkAnagram(st1, st2):
    mp = {}

    for c in st1:
        if c not in mp:
            mp[c] = 1
        else:
            mp[c] += 1
    
    for c in st2:
        if c not in mp:
            return False
        else:
            mp[c] -= 1
            if mp[c] == 0:
                del mp[c]
    
    return True




if __name__ == "__main__":
    st1 = input('Enter string one: ')
    st2 = input('Enter string two: ')
    print(checkAnagram(st1, st2))