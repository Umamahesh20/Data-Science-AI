import functools
#1. Square only positive numbers
#  Given a list of numbers, return the square of each positive number and ignore negative numbers.
nums = [3, -2, 5, -7, 4]
print(list(map(lambda x:x*x,filter(lambda x:x>0,nums))))

# 2. Convert names to initials
#  Given a list of full names, create initials using the first character of each name. 
names = ["Rahul Sharma", "Amit Kumar", "Priya Singh"]
print(list(map(lambda x:''.join(word[0] for word in x.split()),names)))


#3 Find numbers divisible by both 3 and 5 From a list, filter numbers that are divisible by both 3 and 5.
nums = [10, 15, 20, 30, 45, 52]
print(list(filter(lambda x:x%3==0 and x%5==0,nums)))


#4 Extract the last digit of every number
#  Create a list containing the last digit of every number.
nums = [123, 456, 789, 120]
print(list(map(lambda x:x%10,nums)))


#5 Reverse every string 
# Reverse each string in the given list.
words = ["python", "java", "sql"]
print(list(map(lambda x:''.join(reversed(x)), words)))

# 6 Convert Celsius to Fahrenheit 
# Convert every Celsius temperature to Fahrenheit using the formula (C × 9/5) + 32.
celsius = [0, 25, 100, -10]
print(list(map(lambda c:(c*1.8)+32,celsius)))



#7 Find strings having more than 5 characters 
# Filter the strings whose length is greater than 5.
words = ["cat", "python", "banana", "java", "computer"]
print(list(filter(lambda x:len(x)>5,words)))



#8Remove empty strings
#  Remove empty strings from the list.
words = ["hello", "", "python", "", "java"]
print(list(filter(lambda x:x!="",words)))




#9 Convert names to lowercase and remove spaces 
# Convert each name to lowercase and remove all spaces.
names = ["John Doe", "Ravi Kumar", "Data Science"]
print(list(map(lambda x:x.lower().replace(" ", ""),names)))



#10. Find numbers whose square is greater than 100
#  Filter numbers whose square is greater than 100.
nums = [5, 10, 11, -12, 8, 15]
print(list(filter(lambda x:x*x>100,nums)))



#11.Sort strings according to their length Sort the strings from shortest to longest.
words = ["apple", "hi", "banana", "cat"]
print(sorted(words,key=lambda x: len(x)))



#12. Sort numbers according to their last digit 
# Sort the numbers based on their last digit, from smallest last digit to largest.
nums = [23, 41, 15, 32, 19]
print(sorted(nums,key=lambda x:x%10))



#13. Sort words based on their second character 
# Sort the words according to their second character. 
words = ["cat", "apple", "dog", "banana"]
print(sorted(words,key=lambda x:x[1]))



#14. Find the longest word using reduce() 
# Use reduce() with lambda to find the longest word.
from functools import reduce
words = ["cat", "elephant", "dog", "python"]
print(reduce(lambda a,b:a if len(a)>len(b) else b,words))



#15. Find the shortest word using reduce() 
# Use reduce() with lambda to find the shortest word.
from functools import reduce
words = ["python", "is", "very", "powerful"]
print(reduce(lambda a,b:a if len(a)<len(b) else b,words))



#16. Find strings that start and end with the same character 
# Filter strings whose first and last characters are the same. 
words = ["apple", "banana", "sky", "education"]
print(list(map(lambda word:sum(1 for ch in word if ch in "aeiou"),words)))




#16. Count vowels in each word 
# For every word, count the vowels a, e, i, o, u. 
words = ["radar", "python", "level", "hello", "abcba"]
print(list(filter(lambda x:x[0]==x[-1],words)))




#18. Extract integers from mixed data
#  From a mixed list, keep only integer values.
data = [10, "hello", 25, "python", 40, "java"]
print(list(filter(lambda x:isinstance(x,int),data)))




#19. Create 'number:square' strings 
# Convert every number into the format number:square.
nums = [2, 3, 4, 5]
print(list(map(lambda x:f"{x}:{x*x}",nums)))

# 20. Find palindrome numbers 
# Filter numbers that read the same forwards and backwards.
nums=[121, 123, 444, 567, 909, 100]
print(list(filter(lambda x: str(x) == ''.join(reversed(str(x))), nums)))

# 21. Find numbers whose first digit equals their last digit 
# Filter numbers whose first digit and last digit are the same.
nums1=[121, 234, 343, 450, 454, 5678]
print(list(filter(lambda x: str(x)[0] == str(x)[-1],nums1)))

# 22. Calculate the sum of digits of every number
#  For every number, calculate the sum of its digits.
li1 = [123, 456, 89, 1001]
print(list(map(lambda x: sum(int(digit) for digit in str(x)), li1)))

# 23. Find words containing at least two vowels
#  Filter words that contain at least two vowels.
words=["cat", "apple", "sky", "banana", "python", "Education"]
print(list(filter(lambda x: sum(1 for char in x if char.lower() in 'aeiouAEIOU') >= 2, words)))
# 24. Create 'Name-Length' strings
#  Convert each name into the format Name-Length.
WORDS=["Ravi", "Python", "Java"]
print(list(map(lambda x: f"{x}-{len(x)}",WORDS)))

# 25. Find the second-largest number using reduce()
# Use reduce() with lambda to find the second-largest distinct number. Do not use sorted() or max().
L3=[10, 25, 8, 40, 30, 40]

result = functools.reduce(
    lambda x, y: (y, x[0]) if y > x[0]
    else (x[0], y) if y > x[1] and y != x[0]
    else x,
    L3,
    (float('-inf'), float('-inf'))
)

print(result[1])

# 26. Calculate the product of all digits of every number
#  For every number, calculate the product of its digits.
l=[123, 234, 405, 99]
print(list(map(lambda x: functools.reduce(lambda a,b:a*b,[int(digit) for digit in str(x)]),l)))

# 27. Create a dictionary from two lists
#  Using two lists of names and marks, create a dictionary mapping each name to its mark.
names = ["A", "B", "C"] 
marks = [85, 72, 91]
print(dict(map(lambda name, mark: (name, mark), names,marks)))

# 28. Filter students using multiple conditions 
# Given tuples of (name, age, marks), keep students whose age is at least 18 AND marks are at least 80.
students=[("Ravi", 22, 85), ("Amit", 17, 90), ("Priya", 21, 72), ("Neha", 19, 88)]
print(list(filter(lambda student: student[1] >= 18 and student[2] >=80, students)))

# 29. Calculate total price including 18% GST
#  Add 18% GST to every price and round the result to 2 decimal places.
l7=[100, 250, 499.99]
print(list(map(lambda price: round(price * 1.18, 2), l7)))


# 30. Classify numbers using nested conditions 
# For every number, produce "Positive-Even", "Positive-Odd", "Negative-Even", "Negative-Odd", or "Zero".
l10=[-5, -2, 0, 3, 8, -11]
print(list(map(lambda x: "Zero" if x==0 else "Positive-Even" if x>0 and x%2==0 else 
               "Positive-odd" if x>0 and x%2!=0 else "Negative-even" if x<0 and x%2==0 else "Negative-odd", l10)))

