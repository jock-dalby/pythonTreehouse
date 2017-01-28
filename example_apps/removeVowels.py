def disemvowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    word_list = list(word)
    for vowel in reversed(word_list):
        if vowel in vowels:
            word_list.remove(vowel)
    return ''.join(word_list)
