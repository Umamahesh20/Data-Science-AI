# #prime number:
# n = int(input("Enter a number: "))
# if n < 2:
#     print("Not a prime number")
# else:
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number") 

# timecomplexity = "O(n)"
# # print next prime number:
# n=int(input("Enter a number: "))
# while True:
#     n += 1
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             break
#     else:
#         print("Next prime number is:", n)
#         break

# n=int(input("Enter a number: "))
# while True:
#     p=True
#     if n<2:
#         p=False
#     else:
#         for i in range(2, int(n**0.5)+1):
#             if n % i == 0:
#                 p=False
#                 break
#     if p:
#         print("Next prime number is:", n)
#         break

# #Reverse a number:
# n=int(input("Enter a number: "))
# rev=0
# while n>0:
#     d=n%10
#     rev=rev*10+d
#     n//=10
# print("Reversed number is:", rev)


# #reverse a string:
# n=input("Enter a string: ")
# n=str(n)
# n=n[::-1]
# print("Reversed string is:", n)

#amstrong number:
n=int(input("Enter a number: "))
temp=n
sum=0
while temp>0:
    d=temp%10
    sum+=d**3
    temp//=10
if sum==n:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")
    