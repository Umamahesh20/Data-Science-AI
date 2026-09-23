#1. Count Characters Count the number of characters in a string without using len(). 
# Input: "hello" Output: 5
s=input("Enter a String: ")
c=0
for char in s:
    c+=1
print("Number of characters:", c)
# 2. Count Vowels Count the number of vowels (a, e, i, o, u) in a string. 
# Input: "education" Output: 5
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
#3. Count Consonants Count the consonants in a string.
#  Input: "python" Output: 5