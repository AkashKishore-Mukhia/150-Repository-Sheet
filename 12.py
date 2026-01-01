def countAlphabets(s):
    vowel = 0
    consonant = 0
    for c in s:
        if c in ['a', 'e', 'i', 'o', 'u']:
            vowel += 1
        elif c != ' ':
            consonant += 1
    
    return [vowel, consonant]




if __name__ == "__main__":
    s = input('Enter the message: ')
    vowel, consonant = countAlphabets(s)
    print('Vowels: {}, Consonants: {}'.format(vowel, consonant))