# k=5
# #squre
# for i in range (1,k+1):
#     for j in range(1,k+1):
#         print("*",end=" ")
#     print()




# # Reactagele
# k=4
# l=8
# for i in range(1,k+1):
#     for j in range(1,l+1):
#         print('*',end=" ")
#     print()

#Triangle:
# k=5 
# for i in range(1,k+1):
#     print(i *'* ')

# print()


#OR


# k=4
# for i in range(1,k+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# k=5 
# for i in range(k,0,-1):
#     print(i *'* ')

# print()

# k=5
# for i in range(k,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


# k=5 
# for i in range(1,k+1):
#     print(" "*(k-1),end=" ")
#     print('*'(2*(i-1))) 

# print()


# k=5
# for i in range(1,k+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# for i in range(k,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()



k=5
for i in range (1,k+1):
    for j in range(k-i):
        print(' ',end=' ')
    for l in range (1,2*i):
        print('*',end=' ')
    print()
for i in range (k-1,0,-1):
    for j in range(k-i):
        print(' ',end=' ')
    for l in range (1,2*i):
        print('*',end=' ')
    print()
