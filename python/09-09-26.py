#write a program to define  the 

# def outer():
#     prodname='HP Laptop'
#     def Inner():
#         prodId='hp101'
#         return f'The prod id is {prodId} and the product name is {prodname}'
#     print(Inner())
# outer()



#Write a nested function and define an enclosing variable you collage name and define a local variable your stream of Btech and access both in local scope.

# def collage():
#     collageName='SR INTERNATIONAL INSTITUTE OF TECHNOLOGY'
#     def stream():
#         nonlocal collageName
#         mystream='Btech CSE'
#         return f'The collage name is:{collageName} and  the stream is:{mystream}'
#     print(stream())
# collage()


# def collage():
#     collageName='SR INTERNATIONAL INSTITUTE OF TECHNOLOGY'
#     def stream():
#         nonlocal collageName
#         mystream='Btech CSE'
#         print (f'The collage name is:{collageName} and  the stream is:{mystream}')
#     stream()
# print(collage())

#Write a nested function to genrate email ids for employes 
#for a specific domain , pass domain name as parameter for outer
#function and generate email id inside the inner funcion

# def emailSerives(domain):
#     def empId (empname):

#         return f'{empname}@{domain}'
#     return empId
# domainName=emailSerives('microsoft.com')
# empname=domainName('sumanth')
# print(empname)

#Write nested function to perfrom withdraw in a bank. take balance as enclosing variable and withdraw
# as inner function and pass amount as parameter to the inner funtion and perform the withdraw if balance 
# is greater then amount and also update the balance using nonlocal keyword

def Withdraw():
    balance=10000
    def withdrawAmount(amount):
        nonlocal balance
        if balance>amount:
            balance-=amount
            return f'Withdraw successful. Remaining balance is {balance}'
        else:
            return f'Insufficient balance. Current balance is {balance}'
    print(withdrawAmount(15000))
Withdraw()
