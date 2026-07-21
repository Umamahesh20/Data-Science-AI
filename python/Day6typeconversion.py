# num1=10 #int
# num2=20.5 #float
# total=num1+ num2 #int + float = float

# ## automatic conversion of data type done by python interpreter
# #type conversion
# print("Total:", total)



# bool1=True # by defult True is considered as 1
# num=12
# total=bool1+num # 1+12=13
# print("Total:", total) #13

# bool2=False # by defult False is considered as 0
# total=bool2+num # 0+12=12
# print("Total:", total) #12


# num1=10 #int
# str2="sam" #string
# print("Total:", num1+str2) 

# str1="10" #string
# str2="20" #string
# print(str1+str2) # 1020
 
#  #operation between float and complex
#  fit1=10.5 #float
#  comp1=2+3j #complex
# total=fit1+comp1 #float + complex = complex
# print("Total:", total) # (12.5+3j)

#Type casting
#Type casting is done by the user explicitly when we want to convert one data type to another data type
#Type casting is done by using the built-in functions like int(), float(), str(), complex(), bool() etc.
#Type casting is also called explicit type conversion
#Type casting is done by using the built-in functions like int(), float(), str(), complex(), bool() etc.

#operation between int and float is possible in python
salary=10000 #int
print(float(salary)) #float

#operation between float and int is possible in python
num=12.5 #float
print(int(num)) #int

#operation between int and complex number is possible in python
# com1=3+4j #complex number
# print(int(com1)) #int                     #gives error because we cannot convert complex number to int in python

#operation between int and complex number is possible in python
int1=10 #int
print(complex(int1)) #complex

#operation between int and string is possible in python
price=1000 #int
print(str(price)) #str
print(type(str(price))) #str

#operation between list and tuple is possible in python
list1=[1,2,3,4,5] #list
# print(tuple(list1)) #tuple
print(set(list1)) #set

#operation between tuple and list is possible in python
tuple1=(1,2,3,4,5) #tuple
print(list(tuple1)) #list

#Operation between int and dict is possible in python
# num1 = 10 #int
# print(dict(num1))                      #gives error because we cannot convert int to dict in python



#range
# list1=list(range(1,11)) #list
# print(list1) #list

print(list(range(1,11,2))) #list

#it will take as a end and start the value from 0
#print(list(range(10))) #list

#negative range 
print(list(range(20,0,-10))) #list


#len():It return the number of items in the sequence. It can be used with strings, lists, tuples, sets, and dictionaries.
# str1="Hello, World!"
# print(len(str1)) #13

# list1=[1,2,3,4,5]
# print(len(list1)) #5

# tuple1=(1,2,3,4,5)
# print(len(tuple1)) #5

# set1={1,2,3,4,5}
# print(len(set1)) #5

# dict1={"a":"venk","b":2,"c":3}
# print(len(dict1)) #3