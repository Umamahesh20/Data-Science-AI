#Mutable

list1=[1,2,3,4,5] #list
print(list1) #list
print(id(list1)) #id of list1
list1+=[6,7,8,9,10] #list
print(list1) #list
print(id(list1)) #id of list1


int1=10 #int
print(int1) #int
print(id(int1)) #id of int1
int1+=10 #int
print(int1) #int
print(id(int1)) #id of int1

# checking immutability of float and complex numbers

float1=10.5 #float
print(float1) #float
print(id(float1)) #id of float1
float1+=10.5 #float
print(float1) #float
print(id(float1)) #id of float1

complex1=2+3j #complex
print(complex1) #complex
print(id(complex1)) #id of complex1
complex1+=2+3j #complex
print(complex1) #complex
print(id(complex1)) #id of complex1

string1='Hello' #string
print(string1) #string
print(id(string1)) #id of string1
string1+=' World' #string
print(string1) #string
print(id(string1)) #id of string1

#since set and dictinary are unordered we cannot use += for that

set1={'sumanth','venkatesh','sameer','uma','sai'} #set
print(id(set1)) #id of set1
set1 |= {'mouni','vyshu'} #set
print(set1) #set
print(id(set1)) #id of set1

dict1={'name':'uma','age':25,'gender':'male'} #dict
print(id(dict1)) #id of dict1
dict1.update({'city':'hyderabad','state':'telangana'}) #dict
print(dict1) #dict
dict1 |= {'country':'india'} #dict
print(dict1) #dict
print(id(dict1)) #id of dict1


#input() function: It is used to take input from the user..
#by default input() function takes input as string. 

name=input("Enter your name: ") #string
print(f"Hello {name}, Welcome to Python Programming!")

num1=input("Enter a number: ") #string
num2=input("Enter another number: ") #string
print(num1+num2) #integer addition

#checking arithmetic operators:

num1=int(input("Enter a number1: ")) 
num2=int(input("Enter a number2: ")) 
print(f'sum of {num1} and {num2} is: {num1+num2}') #integer addition
print(f'difference of {num1} and {num2} is: {num1-num2}') #integer subtraction
print(f'product of {num1} and {num2} is: {num1*num2}') #integer multiplication
print(f'division of {num1} and {num2} is: {num1/num2}') #integer division
print(f'floor division of {num1} and {num2} is: {num1//num2}') #integer floor division
print(f'modulus of {num1} and {num2} is: {num1%num2}') #integer modulus
