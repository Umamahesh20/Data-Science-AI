# str1='education'
# uniChars={char for char in str1}
# print(uniChars)

# vowelChar={char for char in  str1 if char in 'aeiou'}
# print(vowelChar)

# #Note in order to pass a string of multiple lines i.e. paragraph as one single string ,we can 
# #use either 


# bio='''My name is Umamaheswararao '''
# uniword={word for word in bio}
# print(uniword)

#dict comprehensions
nums=[4,7,9,2,-1,3]
cube={num: num**3 for num in nums}
print(cube)

words=['python', 'Aritificial Intelligence ', 'Machine Learn', 'Java', 'C++']
wordLen={len(word): word for word in words if len(word)>5}
print(wordLen)