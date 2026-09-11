# #ord
# # print(ord('-'))
# # print(chr(45))

# #write a program to convert a character from uppercase to lowercase 

# char=input('Enter character:')
# lower=chr(ord(char)+32)
# print(lower)

# def lowertoUpper(char):
#     if 'a'<=char<='z':
#         upper=chr(ord(char)-32)
#         print(upper)
#     else:
#         print('error')


# lowertoUpper('k')


# #write a function  to swapcase of each character in a string
# def swapcase(str):
#     newstr=''
#     for char in str:
#         if 'a'<=char<='z':
#             newstr+=chr(ord(char)-32)
#         elif 'A'<=char<='Z':
#             newstr+=chr(ord(char)+32)
#             return newstr
#     return newstr
# str=input('Enter String:')
# print(swapcase(str))



# #enumerate():
# name=['sumanth','usha sri','venkatesh','madhesh','roshini']
# for rollNo,name in enumerate(name,101):
#     print(f'{rollNo}:{name}')


# write a program to assign empids to each and every 
#employee name using enumerate function 
# def empIdAssign(empnames):
#     companyID='VASU'
#     for empId,empname in enumerate(empnames,101):
#         print(F'Employee name {empname} got Employee ID:{companyID+str (empId)}')
# empIdAssign(['sumanth','usha sri','venkatesh','madhesh','roshini'])


emp=['sumanth','usha sri','venkatesh','madhesh','roshini']
sals=[60000,40000,50000,70000,80000]
place=['Hyderabad', 'Guntur','Vijayawada','Bangalore','Chennai']
for empname,salaly,city in zip(emp,sals,place):
    print(f'Employee name:{empname} and salary is:{salaly} and palce is:{city}')

# nenumerate() and zip()  together
#write a funtion to generate product ids for list of products withn enumerate function also
#  and also combine product  name with their prices and caegories with zip funcion 
