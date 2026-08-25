# #nested for loop:
# for i in range (1,5):
#     for j in range(1,5):
#         print(i,j)

# WAP TO PRINT ALL THE TABLES OF NUMBER 1 TO 10


# print('Table from 1 to 10')
# for i in range (1,11):
#     print(f'Table of {i} is:')
#     for j in range(1,11):
#         print(f'{i}X{j}={i*j}')

# # WAP TO PRINT COMMON ITEMS BETWEEN TWO Items using two for loop

# from numpy import matrix


# l1=['chicken fried rice', 'Noodles', 'Manchuria',]
# l2=['chiken briyani', 'Soup','chicken 65','chicken Majestic ', 'Ice cream ']
# c=[]
# for item1 in l1:
#     for item2 in l2:
#         c += [item1]
# print("commen item is:")


# # matrix addtion
# matrix=[2,4,5],
# [6,4,3],
# [7,8,4]


n=int(input("enter no of rows:"))
for i in range (1, n+1):
    for j in range(i):
        print('hello',end=" ")
    print()


n=int(input("enter no of rows:"))
for i in range (n,0,-1 ):
    for j in range(i,i+1):
        print('*',end=" ")
    print()
