def count_char(s):
    count = 0
    i = 0
    while i < len(s):
        count += 1
        i += 1
    return count
s = input("Enter a string: ")
print(count_char(s))


# output:
# Enter a string: Umamahesh
# 9


def vowels_count(s):
    i=0
    count=0
    while i<len(s):
        if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or\
            s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
            count+=1
        i+=1
    return count
s=input("Enter the string: ")
print(f'The given string has {vowels_count(s)} vowels')

# Output:
# Enter the string: Umamahesh
# The given string has 4 vowels



def consonants_count(s):
    i = 0
    count = 0
    while i < len(s):
        if s[i]!='a' and s[i]!='e' and s[i]!='i' and s[i]!='o' and s[i]!='u' and\
           s[i]!='A' and s[i]!='E' and s[i]!='I' and s[i]!='O' and s[i]!='U':
            count += 1
        i += 1
    return count
s = input("Enter the string: ")
print(f"The given string has {consonants_count(s)} consonants")

# Output:
# Enter the string: Umamahesh
# The given string has 5 consonants


def reversing(s):
    i = len(s) - 1
    result = ""
    while i >= 0:
        result += s[i]
        i -= 1
    return result
s = input("Enter the string: ")
# print(f"The reversed string is {reversing(s)}")
# Output:
# Enter the string: Umamahesh
# The reversed string is hsehamamU



def palindrome(s):
    i = len(s) - 1
    result = ""
    while i >= 0:
        result += s[i]
        i -= 1
    if s == result:
        return f'The given string {s} is a palindrome'
    else:
        return f'The given string {s} is not a palindrome'
s=input('Enter the string: ')
print(palindrome(s))

# OutPut:
# Enter the string: refer
# The given string refer is a palindrome


def count_char(s, ch):
    i = 0
    count = 0
    while i < len(s):
        if s[i] == ch:
            count += 1
        i += 1
    return count
s = input('Enter the string: ')
ch = input('Enter the character: ')
print(f'The character {ch} occurs {count_char(s, ch)} times')

# Output:
# Enter the string: Umamahesh
# Enter the character: a
# The character a occurs 2 times


def uppercase(s):
    i = 0
    result = ""
    while i < len(s):
        if 'a' <= s[i] <= 'z':
            result += chr(ord(s[i]) - 32)
        else:
            result += s[i]
        i += 1
    return result
s = input("Enter the string: ")
print(f"Uppercase string: {uppercase(s)}")

# Output:
# Enter the string: umamahesh
# Uppercase string: UMAMAHESH


def lowercase(s):
    i = 0
    result = ""
    while i < len(s):
        if 'A' <= s[i] <= 'Z':
            result += chr(ord(s[i]) + 32)
        else:
            result += s[i]
        i += 1
    return result
s = input("Enter the string: ")
print(f"lowercase string: {lowercase(s)}")

# Output:
# Enter the string: UMAMAHESH
# lowercase string: umamahesh


def print_char(s):
    i = 0
    while i < len(s):
        print(s[i])
        i += 1
s = input("Enter the string: ")
print_char(s)

# Output:
# Enter the string: uma
# u
# m
# a



def find_char(s, ch):
    i = 0
    while i < len(s):
        if s[i] == ch:
            return "Found"
        i += 1
    return "Not Found"
s = input("Enter the string: ")
ch = input("Enter the character: ")
print(find_char(s, ch))

# Output:
# Enter the string: Umamahesh
# Enter the character: h
# Found


def count_digits(s):
    i = 0
    count = 0
    while i < len(s):
        if '0' <= s[i] <= '9':
            count += 1
        i += 1
    return count
s = input("Enter the string: ")
print(f"The string has {count_digits(s)} digits")

# Output:
# Enter the string: ammulu752
# The string has 3 digits



def count_alphabets(s):
    i = 0
    count = 0
    while i < len(s):
        if ('a' <= s[i] <= 'z') or ('A' <= s[i] <= 'Z'):
            count += 1
        i += 1
    return count
s = input("Enter the string: ")
print(f"The string has {count_alphabets(s)} alphabets")

# Output:
# Enter the string: Sameer 
# The string has 6 alphabets


def remove_spaces(s):
    i = 0
    result = ""
    while i < len(s):
        if s[i] != ' ':
            result += s[i]
        i += 1
    return result
s = input("Enter the string: ")
print(remove_spaces(s))

# Output:
# Enter the string: Uma Maheswara Rao
# UmaMaheswaraRao


def first_char(s):
    i = 0
    while i < len(s):
        return s[i]
s = input("Enter the string: ")
print(f"The first character is {first_char(s)}")

# Output:
# Enter the string: SumanthTeja
# The first character is S


def last_char(s):
    i = 0
    while i < len(s):
        i += 1
    return s[i - 1]
s = input("Enter the string: ")
print(f"The last character is {last_char(s)}")

# Output:
# Enter the string: SumanthTeja
# The last character is a