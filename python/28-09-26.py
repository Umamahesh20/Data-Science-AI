# # even and odd list
# m=int(input('Enter starting number'))
# n=int(input('Enter ending number'))
# temp=m
# evencount=0
# oddcount=0
# evenlist=[]
# oddlist=[]
# while temp<=n:
#     if temp&2==0:
#         evenlist+=[temp]
#         evencount+=1
#     else:
#         oddlist=oddlist+[temp]
#         oddcount+=1
#     temp+=1
# print(f'The list of even number from {m} t {n} is:{evenlist}')
# print(f'the  number of even number{evencount} the nuber of odd count is{oddcount} ')
# print(f'The list of even number from {m} t {n} is:{oddlist}')


# reverse string
# s=input('enter the string')
# print(s[::-1])

# s=input('enter string ')
# rev='' 
# i=0
# while i<len(s):
#     rev=s[i]+rev
#     i+=1
# print(rev)

# paladrom
s=input('enter string ')
rev='' 
i=0
while i<len(s):
    rev=s[i]+rev
    i+=1
if s==rev:
    print('The given stirng is palindrome ')
else:
    print('The given stirng is not palindrome ')