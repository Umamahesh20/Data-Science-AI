#sorting if list of name based o their length

# names=['umamaheswararo','sumanthteja','venkatesh','abishya']

# laf= lambda name : len(name)
# sortednames=sorted(names, key=laf, reverse=True)
# print(sortednames)


# Marks=[('Ram',89),('Rahul',32),('Shreya',90),('smriti',56),('Gangadhar',99)]

# lat= lambda record :record[1]
# sortedMarks=sorted(Marks, key=lat)
# print(sortedMarks)



# empRec={'Vasudha': 45000, 'Rasagna': 90000, 'venkat': 12000, 'shanker': 110000, 'Sumanth': 10000000}
# print()
# lat= lambda record :record[1]
# sortedSalary=sorted(empRec.items(), key=lat, reverse=True)
# print(sortedSalary)

from functools import reduce
#reduce()

# nums=[1,2,3,4,5]
# # lambfun= lambda num1, num2:num1+num2
# # Redu=reduce(lambfun,nums)
# # print(Redu)

# lambfun= lambda n1,n2:n1*n2
# redsqe=reduce(lambfun,nums)
# print(redsqe)


# nums=(45,76,34,12,89,90,56,345,876,11,22,10)
# lamfun=lambda n1,n2:n1 if n1>n2 else n2
# greatestEle=reduce(lamfun,nums, 1000)
# print(greatestEle)



L3=[10, 25, 8, 40, 30, 40]

result = reduce(
    lambda x, y: (y, x[0]) if y > x[0]
    else (x[0], y) if y > x[1] and y != x[0]
    else x,
    L3,
    (float('-inf'), float('-inf'))
)

print(result[1])