# #funcion for sum of two numbers
# def Twonum(n1,n2):
#     return n1+n2

# print(Twonum(5,3))

# #one line function
# print((lambda x,y:x+y)(7,4))
# print(( lambda n1,n2:n1*n2)(7,3))


# print((lambda x,y:x**y)(5,5))

#writ a lambda function to find greatest amount two numbers

# print((lambda n1,n2:f"{n1} is greatest "if n1>n2 else f"{n2}is greatest")(43,76))

#write a lambda function it even or odd 
# print((lambda n:f"{n} is even" if n%2==0 else f"{n}  is odd")(89))

# Write a lambda function to performs num of nums using variable length arguments.
# print((lambda *args:sum(args))(2,3,4,5,6,7,8))

#write a lambda function to convert a temp from celsius to fahrehe

print((lambda c:(c*9/5)+32)(45))

#write a lambda function that smallest amoung three  numbers
print((lambda n1,n2,n3:f"{n1} is smallest" if n1<n2 and n1<n3 else f"{n2} is smallest" if n2<n1 and n2<n3 else f"{n3} is smallest")(76,57,876))
