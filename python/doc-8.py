# # 1. Daily Water Intake
# # Task: Read the amount of water consumed each day for 7 days using a while loop.
# # Find the total water consumed.

# def waterIntake():
#     total = 0
#     i = 1
#     while i <= 7:
#         water = float(input("Enter water consumed on day " + str(i) + ": "))
#         total = total + water
#         i = i + 1
#     return total

# result = waterIntake()
# print("Total water consumed:", result, "liters")

# # 2. Grocery Shopping
# # Task: Read the prices of 10 grocery items using a while loop.
# # Find the total bill amount.

# def groceryBill():
#     total = 0
#     i = 1
#     while i <= 10:
#         price = float(input("Enter price of item " + str(i) + ": "))
#         total = total + price
#         i = i + 1
#     return total

# result = groceryBill()
# print("Total bill amount:", result)

# # 3. Classroom Attendance
# # Task: Read the attendance (Present or Absent) of 20 students.
# # Count how many students are present.

# def attendance():
#     present = 0
#     i = 1
#     while i <= 20:
#         status = input("Enter attendance of student " + str(i) + ": ")
#         if status.lower() == "present":
#             present = present + 1
#         i = i + 1
#     return present

# result = attendance()
# print("Number of students present:", result)

# # 4. Cricket Tournament
# # Task: Read the runs scored in 10 matches.
# # Find the total runs scored.

# def cricketRuns():
#     total = 0
#     i = 1
#     while i <= 10:
#         runs = int(input("Enter runs in match " + str(i) + ": "))
#         total = total + runs
#         i = i + 1
#     return total

# result = cricketRuns()
# print("Total runs:", result)

# # 5. Fuel Station
# # Task: Read the liters of fuel filled by 15 customers.
# # Find the total liters sold.

# def fuelSold():
#     total = 0
#     i = 1
#     while i <= 15:
#         liters = float(input("Enter fuel liters for customer " + str(i) + ": "))
#         total = total + liters
#         i = i + 1
#     return total

# result = fuelSold()
# print("Total liters sold:", result)

# # 6. Employee Salaries
# # Task: Read the salaries of 12 employees.
# # Find the highest salary.

# def highestSalary():
#     highest = 0
#     i = 1
#     while i <= 12:
#         salary = float(input("Enter salary of employee " + str(i) + ": "))
#         if salary > highest:
#             highest = salary
#         i = i + 1
#     return highest

# result = highestSalary()
# print("Highest salary:", result)

# # 7. Bike Mileage
# # Task: Read the mileage of 10 bikes.
# # Find the average mileage.

# def averageMileage():
#     total = 0
#     i = 1
#     while i <= 10:
#         mileage = float(input("Enter mileage of bike " + str(i) + ": "))
#         total = total + mileage
#         i = i + 1
#     return total / 10

# result = averageMileage()
# print("Average mileage:", result)

# # 8. Mobile Recharge
# # Task: Read the recharge amounts of 15 customers.
# # Count how many customers recharged more than ₹500.

# def rechargeCount():
#     count = 0
#     i = 1
#     while i <= 15:
#         amount = float(input("Enter recharge amount of customer " + str(i) + ": "))
#         if amount > 500:
#             count = count + 1
#         i = i + 1
#     return count

# result = rechargeCount()
# print("Customers recharged more than ₹500:", result)

# 9. Electricity Usage
# Task: Read electricity units used by 20 houses.
# Find the total units consumed.

# def electricityUsage():
#     total = 0
#     i = 1
#     while i <= 20:
#         units = float(input("Enter units used by house " + str(i) + ": "))
#         total = total + units
#         i = i + 1
#     return total

# result = electricityUsage()
# print("Total units consumed:", result)

# # 10. Exam Results
# # Task: Read the marks of 30 students.
# # Count how many students passed (marks >= 35).

# def passedStudents():
#     count = 0
#     i = 1
#     while i <= 30:
#         marks = int(input("Enter marks of student " + str(i) + ": "))
#         if marks >= 35:
#             count = count + 1
#         i = i + 1
#     return count

# result = passedStudents()
# print("Number of students passed:", result)

# # 11. Hospital Patients
# # Task: Read the ages of 20 patients.
# # Count how many patients are senior citizens (age >= 60).

# def seniorCitizens():
#     count = 0
#     i = 1
#     while i <= 20:
#         age = int(input("Enter age of patient " + str(i) + ": "))
#         if age >= 60:
#             count = count + 1
#         i = i + 1
#     return count

# result = seniorCitizens()
# print("Senior citizens:", result)

# # 12. Bus Passengers
# # Task: Read the number of passengers entering the bus at 8 stops.
# # Find the total passengers.

# def busPassengers():
#     total = 0
#     i = 1
#     while i <= 8:
#         passengers = int(input("Enter passengers at stop " + str(i) + ": "))
#         total = total + passengers
#         i = i + 1
#     return total

# result = busPassengers()
# print("Total passengers:", result)

# # 13. Cinema Tickets
# # Task: Read the ticket prices of 25 customers.
# # Find the total ticket collection.

# def ticketCollection():
#     total = 0
#     i = 1
#     while i <= 25:
#         price = float(input("Enter ticket price of customer " + str(i) + ": "))
#         total = total + price
#         i = i + 1
#     return total

# result = ticketCollection()
# print("Total ticket collection:", result)

# # 14. Warehouse Boxes
# # Task: Read the weight of 20 boxes.
# # Find the heaviest box.

# def heaviestBox():
#     highest = 0
#     i = 1
#     while i <= 20:
#         weight = float(input("Enter weight of box " + str(i) + ": "))
#         if weight > highest:
#             highest = weight
#         i = i + 1
#     return highest

# result = heaviestBox()
# print("Heaviest box:", result, "kg")

# # 15. Phone Battery
# # Task: Read the battery percentage of 15 phones.
# # Count how many phones have battery below 20%.

# def lowBattery():
#     count = 0
#     i = 1
#     while i <= 15:
#         battery = int(input("Enter battery percentage of phone " + str(i) + ": "))
#         if battery < 20:
#             count = count + 1
#         i = i + 1
#     return count

# result = lowBattery()
# print("Phones below 20% battery:", result)

# # 16. Monthly Expenses
# # Task: Read daily expenses for 30 days.
# # Find the total monthly expense.

# def monthlyExpense():
#     total = 0
#     i = 1
#     while i <= 30:
#         expense = float(input("Enter expense for day " + str(i) + ": "))
#         total = total + expense
#         i = i + 1
#     return total

# result = monthlyExpense()
# print("Total monthly expense:", result)

# # 17. Hotel Room Rent
# # Task: Read the room rent of 12 bookings.
# # Find the highest room rent.

# def highestRoomRent():
#     highest = 0
#     i = 1
#     while i <= 12:
#         rent = float(input("Enter room rent for booking " + str(i) + ": "))
#         if rent > highest:
#             highest = rent
#         i = i + 1
#     return highest

# result = highestRoomRent()
# print("Highest room rent:", result)

# # 18. ATM Withdrawals
# # Task: Read the withdrawal amounts of 15 customers.
# # Count how many customers withdrew more than ₹10000.

# def largeWithdrawals():
#     count = 0
#     i = 1
#     while i <= 15:
#         amount = float(input("Enter withdrawal amount of customer " + str(i) + ": "))
#         if amount > 10000:
#             count = count + 1
#         i = i + 1
#     return count

# result = largeWithdrawals()
# print("Customers who withdrew more than ₹10000:", result)

# # 19. Product Ratings
# # Task: Read the ratings (1-5) of 20 products.
# # Count how many products received a rating of 5.

# def fiveStarProducts():
#     count = 0
#     i = 1
#     while i <= 20:
#         rating = int(input("Enter rating of product " + str(i) + ": "))
#         if rating == 5:
#             count = count + 1
#         i = i + 1
#     return count

# result = fiveStarProducts()
# print("Products with rating 5:", result)

# # 20. Internet Data Usage
# # Task: Read daily internet usage (GB) for 30 days.
# # Find the total data used.

# def dataUsage():
#     total = 0
#     i = 1
#     while i <= 30:
#         data = float(input("Enter data used on day " + str(i) + ": "))
#         total = total + data
#         i = i + 1
#     return total

# result = dataUsage()
# print("Total data used:", result, "GB")

# # 21. Flight Luggage
# # Task: Read the luggage weight of 20 passengers.
# # Count how many passengers have luggage above 15 kg.

# def heavyLuggage():
#     count = 0
#     i = 1
#     while i <= 20:
#         weight = float(input("Enter luggage weight of passenger " + str(i) + ": "))
#         if weight > 15:
#             count = count + 1
#         i = i + 1
#     return count

# result = heavyLuggage()
# print("Passengers with luggage above 15 kg:", result)

# # 22. Water Bottles
# # Task: Read the capacity of 15 water bottles.
# # Find the smallest bottle capacity.

# def smallestBottle():
#     smallest = float('inf')
#     i = 1
#     while i <= 15:
#         capacity = float(input("Enter capacity of bottle " + str(i) + ": "))
#         if capacity < smallest:
#             smallest = capacity
#         i = i + 1
#     return smallest

# result = smallestBottle()
# print("Smallest bottle capacity:", result)

# # 23. Online Orders
# # Task: Read the values of 20 online orders.
# # Count how many orders are above ₹1000.

# def largeOrders():
#     count = 0
#     i = 1
#     while i <= 20:
#         value = float(input("Enter order value " + str(i) + ": "))
#         if value > 1000:
#             count = count + 1
#         i = i + 1
#     return count

# result = largeOrders()
# print("Orders above ₹1000:", result)

# # 24. Rainfall Record
# # Task: Read rainfall (mm) for 12 months.
# # Find the highest rainfall.

# def highestRainfall():
#     highest = 0
#     i = 1
#     while i <= 12:
#         rainfall = float(input("Enter rainfall for month " + str(i) + ": "))
#         if rainfall > highest:
#             highest = rainfall
#         i = i + 1
#     return highest

# result = highestRainfall()
# print("Highest rainfall:", result, "mm")

# # 25. School Fees
# # Task: Read the fees paid by 15 students.
# # Find the total amount collected.

# def schoolFees():
#     total = 0
#     i = 1
#     while i <= 15:
#         fee = float(input("Enter fee paid by student " + str(i) + ": "))
#         total = total + fee
#         i = i + 1
#     return total

# result = schoolFees()
# print("Total fees collected:", result)

# # 26. Car Speeds
# # Task: Read the speed of 20 cars.
# # Count how many cars exceeded 80 km/h.

# def fastCars():
#     count = 0
#     i = 1
#     while i <= 20:
#         speed = float(input("Enter speed of car " + str(i) + ": "))
#         if speed > 80:
#             count = count + 1
#         i = i + 1
#     return count

# result = fastCars()
# print("Cars exceeding 80 km/h:", result)

# # 27. Library Books
# # Task: Read the number of pages in 15 books.
# # Find the book with the maximum pages.

# def maximumPages():
#     maximum = 0
#     i = 1
#     while i <= 15:
#         pages = int(input("Enter pages of book " + str(i) + ": "))
#         if pages > maximum:
#             maximum = pages
#         i = i + 1
#     return maximum

# result = maximumPages()
# print("Maximum pages:", result)

# # 28. Store Inventory
# # Task: Read the stock quantity of 25 products.
# # Count how many products have stock less than 10 units.

# def lowStock():
#     count = 0
#     i = 1
#     while i <= 25:
#         stock = int(input("Enter stock of product " + str(i) + ": "))
#         if stock < 10:
#             count = count + 1
#         i = i + 1
#     return count

# result = lowStock()
# print("Products with stock less than 10:", result)

# # 29. Courier Service
# # Task: Read the parcel weight of 20 customers.
# # Count how many parcels weigh more than 10 kg.

# def heavyParcels():
#     count = 0
#     i = 1
#     while i <= 20:
#         weight = float(input("Enter parcel weight of customer " + str(i) + ": "))
#         if weight > 10:
#             count = count + 1
#         i = i + 1
#     return count

# result = heavyParcels()
# print("Parcels weighing more than 10 kg:", result)

# # 30. Employee Working Hours
# # Task: Read the working hours of 30 employees.
# # Count how many employees worked more than 8 hours.

# def extraWorkingHours():
#     count = 0
#     i = 1
#     while i <= 30:
#         hours = float(input("Enter working hours of employee " + str(i) + ": "))
#         if hours > 8:
#             count = count + 1
#         i = i + 1
#     return count

# result = extraWorkingHours()
# print("Employees who worked more than 8 hours:", result)