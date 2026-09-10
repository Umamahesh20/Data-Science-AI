# #key WORD arguments:

# from functools import total_ordering


# def details(name,course,job):
#     print(f'{name} has done  course in {course} and current work as  {job} ')

# details('venket','Msc','Trainer')
# details(job='Trainer',name='venket',course='Msc')

# #write a funcion to calculate and print total bill of an item based
# #on quantity along with the item name.

# # def bill(item, price, quantity):
# #     total_bill = price * quantity
# #     return f"the item purchased is {item}: quantity = {quantity}, total bill = {total_bill}"

# # print(bill(price=5999))


# def elecBill(units,rate,fixedChar):
#     basicBill=units*rate
#     totalBill=basicBill+fixedChar
#     print(f'You 8used {units} units at a rate of {rate} per unit')
#     print(f'Your perious mounth bill is :{totalBill}')

# elecBill(rate=8,units=420,fixedChar=57)

# # write a funtion whether a person can login into a
# # system based on his credentials and login time.
# def login(username,password,loginTime):
#     if loginTime>10 and loginTime<19:
#         if username=='uma' and password=='sam123':
#             print('Login successful')
#         else:
#             print('Invalid credentials')
#     else:
#         print('Cannot login at this time')

# login(username='uma',password='sam123',loginTime=12)
# login(password='sam123',loginTime=23,username='uma')


# def argCounter(*args):
#     count=0
#     for i in args:
#         count+=1
#     print(f'The number of arguments passed is {count}')

# argCounter(1,2,3,4,5,6,7,8,9,'uma')
# argCounter()

# def sumNprod(*nums):
#     sum=0
#     nums=1
#     prod=1
