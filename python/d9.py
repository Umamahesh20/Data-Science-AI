#Logical operators:
# and

age=21
citizenship='Indian'
if age>=18 and citizenship=='Indian':   
    print("You are eligible to get driving license")  # Output: You are eligible to get driving license 

#or

degree=True
btech=False
print(degree or btech)  # Output: True

#checking whether it is a holiday or not
weekday=False
holiday=True
print(weekday or holiday)  # Output: True


# payment with card or cash or upi
card='no'
cash='no' 
upi='yes'
print(card=='yes' or cash=='yes' or upi=='yes' )


#not

passed=True
print(not passed)

login='yes'
print(not login=='yes')


num=3
num2=range


teslaCeo='elon musk'
spacexCeo='elon musk '
print()


num1=10
print(id(num1))
num2=10.0
print(id(num2))

#Identity operators
#is
num1 = 10
num2 = 20
print(num1 is num2)  # False, num1 and num2 are not the same object


Chinnodu="sumanth"
student=Chinnodu
print(Chinnodu is student)  # True, Chinnodu and student are the same object


developer = "write code"
tester = "test code"
print(developer is not tester)  # True, developer and tester are not the same object

num1 = 10
print(id(num1))  # True, num1 and 10 are the same object
num2 = 10.0
print(id(num2))
print(num1 is not num2)  # True, num1 and num2 are not the same object


#code optimization: The program create only on object for all variables if the object size is within limits 
# if the size of the object go beyond the limit python create different object for each variable.
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 is list2)  # False, list1 and list2 are not the same object
print(list1 == list2)  # True, list1 and list2 have the same values