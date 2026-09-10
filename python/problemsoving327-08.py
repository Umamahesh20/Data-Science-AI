# write a program to print sum and product of number from m to n
# num1=int(input("Enter number"))
# num2=int(input("Enter number"))
# sum=0
# product=1
# if num1 > num2:
#     num1, num2 = num2, num1
# for i in range(num1, num2 + 1):
#     sum+=i
#     product*=i
# print(sum, product)    


# fibonacci series
n=int(input())
a=0
b=1
for i in range(n):
    a,b=b,a+b
print(a,b)