# # # WRITE A PROGRAM  TO GENERATE A LIST OF SQURES OF EACH VALUES IN A LIST

# # nums=[4,5,6,7]
# # # SQNUMS=[]
# # # for i in   nums:
# # #     SQNUMS+=[i*i]


# # SQNUMS=[num*num for num in nums]
# # print(SQNUMS)

# nums=[1,2,3,4,5,6,7,8,9,10]
# evenNum=[num for num in nums if num%2==0]
# print(evenNum)
# oddNum=[num for num in nums if num%2!=0]
# print(oddNum)

# #write a list comprehensions to genrate a 3x3 zero matic
# zeroMatrics=[[0]*3 for i in range(3)  ]
# print(zeroMatrics)
# names=['kiran','sumanth','mahesh','mouni']
# upper=[i.upper() for i in names]
# # print(upper)

# nums=[56,76,23,11,-2,707,43,90,71,77]

# costPrice=[11299,13999,15899,34999,56986]
# #genrate a list of selling prices by adding 10% of each
# #price to itself  using comprehesion.
# selllingPrice=[f'{price*1.1:.2f }'for price in costPrice]
# print(selllingPrice)

emails=['sumanthteja@tesla.com','umamahesh@spacex.com','vyshinavi@oracal.com']
#write a comprehension to generate a list of usernames 
#from emails
username=[email.split('@')[0] for email in emails]
dominname=[email.split('@')[-1] for email in emails]
print(username)
print(dominname)