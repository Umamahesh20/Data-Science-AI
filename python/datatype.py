# Datatypes in Python
str='10'
print(str(str))  # Output: 10

#Numerical Datatypes
# integer: It is a whole number with no decimal point, it can be positive or negative.
#type function type() is used to check the data type

int1=10
age=25
temp=11
Class=11
print(age)  # Output: 25
print(Class)  # Output: 11
print(temp)  # Output: 11
print(type(age))  # Output: <class 'int'>
print(type(Class))  # Output: <class 'int'>
print(type(temp))  # Output: <class 'int'>
print(int1)  # Output: 10
print(type(int1))  # Output: <class 'int'>


#Float:
 # it is a number with decimal point, it is also called as floating point number

percentage= 99.9
print(percentage)  # Output: 99.9
cgpa= 100.0
print(cgpa)  # Output: 100.0
print(type(percentage))  # Output: <class 'float'>
print(type(cgpa))  # Output: <class 'float'>
temperature= 36.6
print(temperature)  # Output: 36.6
print(type(temperature))  # Output: <class 'float'>


#complex: It is a number with real and imaginary part, it is also called as complex number
#number
#real number= the part of complex number with no alphabetic character
#image number= the part of complex number with alphabetic character
complex1= 2+3j
print(complex1)  # Output: (2+3j)
complex2= 4-5j
print(complex2)  # Output: (4-5j)
print(type(complex1))  # Output: <class 'complex'>
print(type(complex2))  # Output: <class 'complex'>


#String Data Type: It is a group of characters enclosed in single or double quotes, it is also called as string

#eg
name= 'uma'
UserName= "uma752"
password= 'uma@123'
print(name)  # Output: uma
print(UserName)  # Output: uma752   
print(password)  # Output: uma@123
print(type(name))  # Output: <class 'str'>
print(type(UserName))  # Output: <class 'str'>
print(type(password))  # Output: <class 'str'>

#Boolean Data Type: This data type store truth values
#truth values: valuesyou get when you excute a condition, it can be either True or False
#eg
print(5==2)  # Output: False
print(5>2)  # Output: True
print(5<2)  # Output: False


#Sequence Data Type: It is a data type which store multiple values in a single variable
#object
#list : It is a collection of values enclosed in square brackets
sem1Marks= [62, 82, 70, 60, 50]
print(sem1Marks)  # Output: [62, 82, 70, 60, 50]
print(type(sem1Marks))  # Output: <class 'list'>

# tuple: it is a collection of values enclosed in parentheses
profle= ('uma', 25, 'male', 'Bangalore')
print(profle)  # Output: ('uma', 25, 'male', 'Bangalore')
print(type(profle))  # Output: <class 'tuple'>
