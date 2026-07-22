#Assignment operators:

name ='Sumanth'
profession ='software engineer'


#augmented assignment operator:
#thses are used to perform some operation and assign the result to the same variable.
#+=, -=, *=, /=, //=, **=, %=
name += 'Teja'
profession += ' and a great developer'
print(name) #string
print(profession) #string


# battary discharge after every app usage
battary=100 #int
battary-=10 #int
battary-=20 #int
battary-=29 #int
battary-=40 #int
print(battary) #int


#augmented multiplication operator:
#*= is the augmented multiplication operator
var=10
var*=10
print(var) 

#double the salary of an employee
salary=50000
salary*=2
print(salary) #int

# adding tax to the price
price=1299
price*=1.1
print(price) #float


# aumented division operator:
# /= is the augmented division operator
#splitting the bill among 4 friends
bill=5768
bill/=4
print(bill) #float

#salary tax deduction
salary=120000
salary/=0.8 # Assuming 20% tax
print(salary) #float

#aumented floor division operator:
# //= is the aumented floor division operator
# disbursing 478 iphones among 12
iphones=478
iphones//=12
print(iphones) #int

#unlocling gun in a game based on points
#such that for every 100 points you unlock a new gun
points=879
points//=100
print(f"Number of guns unlocked: {points}   ")#int


# augmented moudulus operator:
# # %= is the augmented modulus operator
# #checking if a number is even or odd
num=15
num%=2
print(num) #int
if num==0:
    print("The number is even") #int
else:
    print("The number is odd") #int


# **= is the augmented exponentiation operator

# calculating the area of a square 
side=5
side**=2
print(f"The area of the square is: {side}") #int



#comperison operators:
#equal to: ==;

employee=input("Enter your role: ")
print(employee=='admin  ')

#checking password:
savedPassword='admin123'
password=input("Enter your password: ")
print(password==savedPassword)

#!= is the not equal to operator\
state=input("Enter a state which is not a capital: ")
print(state!='Delhi')

# < is the greater than or equal to operator
age=int(input("Enter your age: "))
if age< 18:
    print("You are not eligible to vote")   
else:
    print("You are  eligible to vote")

# checking a person job experience is grater than or equal to 5 years or not
experience=int(input("Enter your job experience in years: "))
print(experience>5)

#task : write 2 real time examples, each of , >= and <= operators and explain them in detail.

# task: write a program to check if a person is exceeding the speed limit or not. If the speed is greater than or equal to 80 km/h, print "You are exceeding the speed limit. Please slow down." Otherwise, print "You are within the speed limit. Drive safely."
speed=int(input("Enter your speed in km/h: "))
if speed>=80:
    print("You are exceeding the speed limit. Please slow down.")
else:
    print("You are within the speed limit. Drive safely.")

# task: write a program to check if a person is eligible for senior citizen benefits. If the age is greater than or equal to 60, print "You are eligible for senior citizen benefits." Otherwise, print "You are not eligible for senior citizen benefits."
age=int(input("Enter your age: "))
if age>=60:
    print("You are eligible for senior citizen benefits.")
else:
    print("You are not eligible for senior citizen benefits.")
    