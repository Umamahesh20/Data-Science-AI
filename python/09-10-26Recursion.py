import time
# def printNums(num):
#     if num<1:
#         print('Time Up')
#         return
#     print(num)
#     # time.sleep(1)
#     printNums(num-1)
# printNums(10)



# def printNums(num):
#     for i in range(1,11):
#         print(i)
# printNums(1)


# def numAdd(num):
#     if num==10:
#         return num
#     return num+numAdd(num+1)
# print(numAdd(1))

# def numfact(num):
#     if num==1:
#           return num
#     return num*numfact(num-1)
# print(numfact(10))

def noofDigit(n):
    if n==0:
        return n
    return 1+noofDigit(n//10)
print(noofDigit(345234567898765434567898765433456789))
