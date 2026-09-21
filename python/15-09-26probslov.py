# problem solving
#Numbers
#1. Check whether a number is spy number or not 
# def spy_number(num):
#     digit=[int(d) for d in str (num)]
#     digitsum=sum(digit)
#     digitproduct=1
#     while num>0:
#         digitproduct*=num%10
#         num//=10
#     if digitsum==digitproduct:
#         print('spy number')
#     else:
#         print('not a spy number')
# num=int(input('Enter number: '))
# spy_number(num)

# def spyNum(num):

#     prod=1
#     sum=0
#     while num>0:
#         digit=num%10
#         sum+=digit
#         prod*=digit
#         num//=10
#     if sum==prod:
#         print(f'{num} is a spy number')
#     else:
#         print(f'{num} is not a spy number')

# num=int(input('Enter number: '))
# spyNum(num)



#write a harshad number
# def Harshad(num):
#     sum=0
#     temp=num
#     while temp>0:
#         digit=temp%10
#         sum+=digit
#         temp//=10
#     if num%sum==0:
#         print(f'number {num}is a harshed number')
#     else:
#         print(f'number {num}is not a harshed number')
# # Harshad(18)

# def Harshad(num):
#     sum=0
#     temp=num
#     while temp>0:
#         digit=temp%10
#         sum+=digit
#         temp//=10
#     if num%sum==0:
#         print(f'number {num}is a harshed number')
#     else:
#         print(f'number {num}is not a harshed number')
# Harshad(18)

# # #armstrong number
# def armstrong(num):
#     sum=0
#     temp=num
#     count=0
#     while temp>0:
#         count+=1
#         temp//=10
#     temp1=num
#     while temp1>0:
#         digit=temp1%10
#         sum+=digit**count
#         temp1//=10

#     if sum==num:
#         print(f'{num} is an armstrong number')
#     else:
#         print(f'{num} is not an armstrong number')
# num=int(input('Enter number: '))

# armstrong(num) 
#armstrong number form 10 armstrong numbers above 10: onle amstrong numbers

# def armstrong(num):
#     sum = 0
#     temp = num
#     count = 0
#     while temp > 0:
#         count += 1
#         temp //= 10
#     temp1 = num
#     while temp1 > 0:
#         digit = temp1 % 10
#         sum += digit ** count
#         temp1 //= 10
#     if sum == num:
#         print(f'{num} is an Armstrong number')
# startnum = int(input('Enter start number: '))
# endnum = int(input('Enter end number: '))
# while startnum <= endnum:
#     armstrong(startnum)
#     startnum += 1





# 4.Automorphic number:
# It is a number whose square ends with the same digits as the number itself .
# def AupNum(num):
#     temp=num
#     square=num**2
#     while temp>0:
#         if temp%10!=square%10:
#             print(f'number {num} is not an automorphoic number')
#             return
#         temp//=10
#         square//=10
#     print(f'number {num} is an automorphic number')
# num=int(input('Enter number: '))
# AupNum(num)


# def AupNum(num):
#     count=0
#     temp=num
#     while temp>0:
#         temp//=10
#         count+=0
#     temp1=num
#     square=num**2
#     while temp1>0:
#         digit= square %10*count

#     if num== digit:
#         print(f'number {num} is  an automorphoic number')
#     else:
#         print(f'number {num} is not an automorphoic number')
# num=int(input('Enter number: '))
# AupNum(num)


