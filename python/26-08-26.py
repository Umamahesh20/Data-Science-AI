# # marks=int(input('Enter marks:'))
# # if marks>=36:
# #     print('pass')
# # else:
# #     print('fails')

# from unittest import result

# marks=int(input('enter marks'))
# result='Pass'if marks>=36 else 'fail'

# print(result)



# n=int(input())
# print("even" if n % 2 == 0 else "odd")

# WRITE A ternary to check whether a number is
# divisible by 3 or not

# n=int(input("enter number:"))
# print("divisible by 3" if n%3==0 else 'not divisable') 


# write a ternary to check whether an order is eligible for 
#free delivery or not


# n=int(input("enter number:"))
# print("free delivery avilable" if n>500 else ' delivery charges applicable') 


# n=int(input("enter number:"))
# print("Divisible by 5 but not by 10 " if n%5==0 and n%10!=0 else 'not ') 

# mark=int(input("enter marks:"))
# print("grade O"if mark>90 else 'grade A' if mark>75 else 'grade b'if mark>35 else 'grade f' )

# from numpy import uint


# signal = input("Enter your signal: ")
# print("GO" if signal == "green" else "Wait" if signal == "yellow" else "Stop")

#write a nested ternary to gerate electricity bill 
# charge 5 rupees per unit if no of units used is less then or equal to 200,
#charge 8 rupees per unit if no f units used is greater than or equal to 400
# charge 12 rupees per unit if no of units used is grater then 500

# units=int(input())
# print(units*(5 if units <= 200 else units*8 if units <= 400 else units* 12 if units > 500 else units*8))
