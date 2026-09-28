# list1=[1,2,3,4,5,6,7,8,9,10]

# tuple1=tuple(num for num in list1 if num%5==0)
# print(tuple1)


# write a comprehension to genrate a tuple from a list of numbers 1 to 50 such that replace all even 
# numbers with 0 and odd number with 1.
# binary=tuple(0 if num%2==0 else 1 for num in range(1,51))
# print(binary)


#write a comprehension to 

# names=['venkat','sumanth','umamaheswararao','rasagna','','vyshanavi','']
# tuple2=tuple(name for name in names if name)
# print(tuple2)

#write a comprehenssion to generate to a tuple from a risto 50  such that the nuber ange of numbers 1 

#divisble by 3 but not5
# `nums=tuple(num for num in range(1,51) if num%3==0 and num%5!=0)
# print(nums)`



#write a tuple comprehension to genrate a tuple of selling price by adding discount such that if prce is 
#grater then 25000 give 11% discount else give 7% discount
prices=[12999,23999,45999,37999,11999,57999,88999]
discount=tuple(price-(price*0.11) if price>25000  else price-(price*0.07) for price in prices  )
print(discount)