# # #nested while loop 
# # i=1
# # while i < 5:
# #     j=1
# #     while j<6:
# #         print(i,j)
# #         j+=1
# #     i+=1

# # write a nested while loop to calculate total and average of 5 student in 5 subjects
# write a nested while loop to calculate total and average of 5 students
# students=1
# while students<=5:
#     total=0
#     marks=1
#     while marks<=5:
#         score=int(input(f"Enter marks of student {students} subject {marks}: "))
#         total+=score
#         marks+=1
#     average=total/5
#     print(f"Total marks of student {students}: {total}")
#     print(f"Average marks of student {students}: {average}")
#     students+=1


#a resturant has 3 customers and each one placed 4 items ordered calculate total bill of each customer with 12%gst
# customers=1
# while customers<=3:
#     totalbill=0
#     items=1
#     while items<=4:
#         price=float(input(f"Enter price of item {items} for customer {customers}: "))
#         totalbill+=price
#         items+=1
#     gst=totalbill*0.12
#     final_bill=totalbill+gst
#     print(f"Total bill for customer {customers} before GST: {totalbill}")
#     print(f"GST amount for customer {customers}: {gst}")
#     print(f"Final bill for customer {customers} after GST: {final_bill}")
#     customers+=1


# #track monthly expense of a person for 3 months for 4 cateories in each month and print the highest expense in all three months
# month=1
# highest=0
# while month <= 3:
#     total=0
#     category=1
#     while category <= 4:
#         expense=float(input(f"Enter expense for month {month} category {category}: "))
#         total+=expense
#         category+=1
#     print(f"Total expense for month {month}: {total}")
#     if total > highest:
#         highest=total
#     month+=1
# print(f"Highest expense: {highest}")

#create a dashbord of runs scored by each player in a test crickte match
# and give man of the match to the person with highest score
# while is true
