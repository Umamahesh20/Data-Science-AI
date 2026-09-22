# # To swap first and last characters of a word
# def swapFAL():
#     word = input("Enter a word: ")
#     if len(word) < 2:
#         return word    
#     chars = list(word)
    
#     chars[0], chars[-1] = chars[-1], chars[0]
#     return "".join(chars)
# print(swapFAL())

def count_vowels_consonants(s):
    vowels = 0
    consonants = 0
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
            vowels += 1
        elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
            consonants += 1
        i += 1
    print("Vowels:", vowels)
    print("Consonants:", consonants)
s = input("Enter a string: ")
count_vowels_consonants(s)