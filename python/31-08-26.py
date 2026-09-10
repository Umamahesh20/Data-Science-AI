# def add():      #funtion declaration
#     num1=int(input('Enter a number:'))
#     num2=int(input('Enter a another number:')) #define
#     print(num1+num2)
# #call the function
# add()


# #declared a function but not defined it
# def testFun():
#     pass

#write a function is even or odd

# def evenORodd():
#     n1=int(input('Enter a number'))
#     if n1%2==0:
#         print(f'{n1} is even')
#     else:
#         print(f'{n1} is odd')
# evenORodd()


from math import factorial


# def Oddnumbers():

#     for i in range (1,51):
#         if i%2!=0:
#             print(i)
# Oddnumbers()


# def prime():
#     n=int(input('enter a number'))
#     count=0
#     for i in range (n):
#         if n%i==0:
#             count+=1

#     if count==2:
#         print(f'The number {n} is prime')
#     else:
#         print(f'The number {n} is not prime')
# prime()

def fact():
    num=int(input())
    temp=1
    while num>=1:
        temp*=num
        num-=1
    return temp
    print (f'factorial of {num} is {factorial(num)}')
fact()
