# #for loop
# for i in range(5):
#     print(i) #int
#     print('umamahesh') #str


#write a program with for loop and range to print  number n to 1 in reverse order
# n=int(input("Enter a number: "))
# for i in range(n,0,-1):
#     print(i) #int

# write a program to bring indvidual characters in a string

# s='data science' 
# for i in s:
#     print(i) #str

# name=['uma','mahesh','kumar']
# for i in name:
#     print(i) #str  


# for i in range(1,11):
#     if i%2==0:
#         print(f"{i} is even") #int

# even=[i for i in range(1,11) if i%2==0]
# print(even) #list

# evennum=[]
# for i in range(1,11):
#     if i%2==0:
#         evennum+=[i]
# print(evennum) #list

# # write a program all odd numbers in a list from 1 to n
# odd=[]
# for i in range(1,11):
#     if i%2==1:
#         odd+=[i]
# print(odd) #list

# write a program calculate total marks of a student 

# marks=[50,56,60,55,70,80]
# total=0
# for i in marks:
#     total+=i
# print(f"Total marks of a student is: {total}") #int:

# WAP to count number of items in a bed
bag=['shirt','pant','t-shirt','toothpaste','water bottle', 'power bank']
count=0
for i in bag:
    count+=1    
print(f"Total items in a bag is: {count}") #int
