# #area of square
# side = float(input("Enter the length of the side of the square: "))
# area = side*side
# #:.nf determines how many decimal values should be returned. 
# #after decimal point.
# # print(f"The area of the square is: {area:.2f}")

# # WAP to calculate the area of a rectangle
# L=float(input("Enter the length of the rectangle: "))
# B=float(input("Enter the breadth of the rectangle: "))
# A=L*B
# print(f"The area of the rectangle is: {A:.2f}")

# # WAP to calculate the area of a TRIANGLE
# H=int(input("Enter the height of the triangle: "))
# B=int(input("Enter the base of the triangle: "))
# A=0.5*H*B
# print(f"The area of the triangle is: {A:.2f}")

# # WAP to calculate the area of a circle
# R=float(input("Enter the radius of the circle: "))
# A=3.14*R*R
# print(f"The area of the circle is: {A:.2f}")


# # perimeter of square
# s=float(input("Enter the length of the side of the square: "))
# P=4*s
# print(f"The perimeter of the square is: {P:.2f}")

# # perimeter of rectangle
# L=float(input("Enter the length of the rectangle: "))
# B=float(input("Enter the breadth of the rectangle: "))
# P=2*(L+B)
# print(f"The perimeter of the rectangle is: {P:.2f}")

# # #perimeter of triangle
# s1=float(input("Enter the length of the first side of the triangle: "))
# s2=float(input("Enter the length of the second side of the triangle: "))
# s3=float(input("Enter the length of the third side of the triangle: "))
# p=s1+s2+s3
# print(f"The perimeter of the triangle is: {p:.2f}")
# h=float(input("Enter the height of the triangle: "))
# b=float(input("Enter the base of the triangle: "))
# p=2*(h+b)
# print(f"The perimeter of the triangle is: {p:.2f}")

# #perimeter of circle
# r=float(input("Enter the radius of the circle: "))
# p=2*3.14*r
# print(f"The perimeter of the circle is: {p:.2f}")

# check whether  the given three sides can form a triangle or not
s1=float(input("Enter the length of the first side of the triangle: "))
s2=float(input("Enter the length of the second side of the triangle: "))
s3=float(input("Enter the length of the third side of the triangle: "))
if (s1+s2>s3) and (s2+s3>s1) and (s1+s3>s2):
    print("The given sides can form a triangle.")
else:
    print("The given sides cannot form a triangle.")

#WAP TO CALUATE TOTAL MARK OF SUDENTS
marks=[55,76,98,34,54,100]

total=0
for mark in marks:
    total+=mark
print(f'The total marks are:{total}')
