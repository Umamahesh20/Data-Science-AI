# # Q1. Weekly Attendance
# # Read attendance of an employee for 7 days and count present days

# def weeklyAttendance():
#     count = 0

#     for i in range(7):
#         status = input("Enter attendance: ")

#         if status.lower() == "present":
#             count = count + 1

#     return count

# result = weeklyAttendance()
# print("Present Days:", result)


# # Q2. Grocery Bill
# # Read prices of 10 grocery items and calculate total bill

# def groceryBill():
#     total = 0

#     for i in range(10):
#         price = float(input("Enter price: "))
#         total = total + price

#     return total

# result = groceryBill()
# print("Total Bill:", result)


# # Q3. Classroom Average
# # Read marks of 20 students and calculate average

# def classroomAverage():
#     total = 0

#     for i in range(20):
#         marks = float(input("Enter marks: "))
#         total = total + marks

#     average = total / 20
#     return average

# result = classroomAverage()
# print("Average Marks:", result)


# # Q4. Highest Temperature
# # Read temperatures of 7 days and find highest temperature

# def highestTemperature():
#     highest = float('-inf')

#     for i in range(7):
#         temperature = float(input("Enter temperature: "))

#         if temperature > highest:
#             highest = temperature

#     return highest

# result = highestTemperature()
# print("Highest Temperature:", result)


# # Q5. Lowest Salary
# # Read salaries of 15 employees and find lowest salary

# def lowestSalary():
#     lowest = float('inf')

#     for i in range(15):
#         salary = float(input("Enter salary: "))

#         if salary < lowest:
#             lowest = salary

#     return lowest

# result = lowestSalary()
# print("Lowest Salary:", result)


# # Q6. Even Seat Numbers
# # Read 25 seat numbers and count even numbers

# def evenSeats():
#     count = 0

#     for i in range(25):
#         seat = int(input("Enter seat number: "))

#         if seat % 2 == 0:
#             count = count + 1

#     return count

# result = evenSeats()
# print("Even Seat Numbers:", result)


# # Q7. Cricket Runs
# # Read runs scored in 10 matches and find total runs

# def cricketRuns():
#     total = 0

#     for i in range(10):
#         runs = int(input("Enter runs: "))
#         total = total + runs

#     return total

# result = cricketRuns()
# print("Total Runs:", result)


# # Q8. Bus Passengers
# # Read passengers entering bus at 8 stops and find total

# def busPassengers():
#     total = 0

#     for i in range(8):
#         passengers = int(input("Enter passengers: "))
#         total = total + passengers

#     return total

# result = busPassengers()
# print("Total Passengers:", result)


# # Q9. Mobile Recharge
# # Read recharge amount of 12 customers and count amounts above 500

# def mobileRecharge():
#     count = 0

#     for i in range(12):
#         amount = float(input("Enter recharge amount: "))

#         if amount > 500:
#             count = count + 1

#     return count

# result = mobileRecharge()
# print("Customers Above ₹500:", result)


# # Q10. Online Orders
# # Read value of 20 orders and count orders above 1000

# def onlineOrders():
#     count = 0

#     for i in range(20):
#         amount = float(input("Enter order value: "))

#         if amount > 1000:
#             count = count + 1

#     return count

# result = onlineOrders()
# print("Orders Above ₹1000:", result)


# # Q11. Water Bottles
# # Read capacity of 15 water bottles and find smallest capacity

# def waterBottles():
#     smallest = float('inf')

#     for i in range(15):
#         capacity = float(input("Enter bottle capacity: "))

#         if capacity < smallest:
#             smallest = capacity

#     return smallest

# result = waterBottles()
# print("Smallest Capacity:", result, "ml")


# # Q12. Electricity Consumption
# # Read electricity units of 10 houses and find total units

# def electricityConsumption():
#     total = 0

#     for i in range(10):
#         units = float(input("Enter electricity units: "))
#         total = total + units

#     return total

# result = electricityConsumption()
# print("Total Units Consumed:", result)


# # Q13. Exam Pass Count
# # Read marks of 30 students and count students who passed

# def examPassCount():
#     count = 0

#     for i in range(30):
#         marks = int(input("Enter marks: "))

#         if marks >= 35:
#             count = count + 1

#     return count

# result = examPassCount()
# print("Students Passed:", result)


# # Q14. Rainfall Record
# # Read rainfall of 12 months and find highest rainfall and month number

# def rainfallRecord():
#     highest = float('-inf')
#     month = 0

#     for i in range(1, 13):
#         rainfall = float(input("Enter rainfall for month " + str(i) + ": "))

#         if rainfall > highest:
#             highest = rainfall
#             month = i

#     return highest, month

# result, month = rainfallRecord()
# print("Highest Rainfall:", result, "mm")
# print("Month Number:", month)


# # Q15. Hospital Patients
# # Read ages of 20 patients and count senior citizens

# def hospitalPatients():
#     count = 0

#     for i in range(20):
#         age = int(input("Enter age: "))

#         if age >= 60:
#             count = count + 1

#     return count

# result = hospitalPatients()
# print("Senior Citizens:", result)


# # Q16. Library Books
# # Read pages of 10 books and find maximum pages

# def libraryBooks():
#     maximum = 0

#     for i in range(10):
#         pages = int(input("Enter number of pages: "))

#         if pages > maximum:
#             maximum = pages

#     return maximum

# result = libraryBooks()
# print("Maximum Pages:", result)


# # Q17. Bike Mileage
# # Read mileage of 15 bikes and calculate average mileage

# def bikeMileage():
#     total = 0

#     for i in range(15):
#         mileage = float(input("Enter mileage: "))
#         total = total + mileage

#     average = total / 15
#     return average

# result = bikeMileage()
# print("Average Mileage:", result, "km/l")


# # Q18. Employee Bonus
# # Read salaries of 20 employees and count employees eligible for bonus

# def employeeBonus():
#     count = 0

#     for i in range(20):
#         salary = float(input("Enter salary: "))

#         if salary < 50000:
#             count = count + 1

#     return count

# result = employeeBonus()
# print("Employees Eligible for Bonus:", result)


# # Q19. Fuel Filling Station
# # Read liters of fuel filled by 10 customers and find total liters

# def fuelStation():
#     total = 0

#     for i in range(10):
#         liters = float(input("Enter liters of fuel: "))
#         total = total + liters

#     return total

# result = fuelStation()
# print("Total Fuel Sold:", result, "Liters")


# # Q20. Product Ratings
# # Read ratings of 25 products and count products rated 5

# def productRatings():
#     count = 0

#     for i in range(25):
#         rating = int(input("Enter rating: "))

#         if rating == 5:
#             count = count + 1

#     return count

# result = productRatings()
# print("Products Rated 5 Stars:", result)


# # Q21. Hotel Room Rent
# # Read room rent of 12 bookings and find highest rent

# def hotelRoomRent():
#     highest = 0

#     for i in range(12):
#         rent = float(input("Enter room rent: "))

#         if rent > highest:
#             highest = rent

#     return highest

# result = hotelRoomRent()
# print("Highest Room Rent:", result)


# # Q22. ATM Transactions
# # Read withdrawal amounts of 15 customers and count withdrawals above 10000

# def atmTransactions():
#     count = 0

#     for i in range(15):
#         amount = float(input("Enter withdrawal amount: "))

#         if amount > 10000:
#             count = count + 1

#     return count

# result = atmTransactions()
# print("Customers Withdrawing More Than ₹10000:", result)


# # Q23. Internet Data Usage
# # Read daily internet usage for 30 days and find total data used

# def internetDataUsage():
#     total = 0

#     for i in range(30):
#         data = float(input("Enter data used in GB: "))
#         total = total + data

#     return total

# result = internetDataUsage()
# print("Total Data Used:", result, "GB")


# # Q24. Car Speeds
# # Read speeds of 20 cars and count cars above 80 km/h

# def carSpeeds():
#     count = 0

#     for i in range(20):
#         speed = float(input("Enter car speed: "))

#         if speed > 80:
#             count = count + 1

#     return count

# result = carSpeeds()
# print("Cars Above 80 km/h:", result)


# # Q25. Cinema Tickets
# # Read ticket prices of 30 customers and find total collection

# def cinemaTickets():
#     total = 0

#     for i in range(30):
#         price = float(input("Enter ticket price: "))
#         total = total + price

#     return total

# result = cinemaTickets()
# print("Total Ticket Collection:", result)


# # Q26. Warehouse Boxes
# # Read weight of 20 boxes and find heaviest box

# def warehouseBoxes():
#     heaviest = 0

#     for i in range(20):
#         weight = float(input("Enter box weight: "))

#         if weight > heaviest:
#             heaviest = weight

#     return heaviest

# result = warehouseBoxes()
# print("Heaviest Box:", result, "kg")


# # Q27. Phone Battery Levels
# # Read battery percentage of 15 phones and count phones below 20%

# def phoneBattery():
#     count = 0

#     for i in range(15):
#         battery = float(input("Enter battery percentage: "))

#         if battery < 20:
#             count = count + 1

#     return count

# result = phoneBattery()
# print("Phones Below 20% Battery:", result)


# # Q28. Daily Expenses
# # Read daily expenses for 30 days and find total monthly expense

# def dailyExpenses():
#     total = 0

#     for i in range(30):
#         expense = float(input("Enter daily expense: "))
#         total = total + expense

#     return total

# result = dailyExpenses()
# print("Total Monthly Expense:", result)


# # Q29. Flight Luggage
# # Read luggage weight of 20 passengers and count luggage above 15 kg

# def flightLuggage():
#     count = 0

#     for i in range(20):
#         weight = float(input("Enter luggage weight: "))

#         if weight > 15:
#             count = count + 1

#     return count

# result = flightLuggage()
# print("Passengers With Luggage Above 15 kg:", result)


# # Q30. Store Inventory
# # Read stock quantity of 25 products and count products with stock less than 10

# def storeInventory():
#     count = 0

#     for i in range(25):
#         stock = int(input("Enter stock quantity: "))

#         if stock < 10:
#             count = count + 1

#     return count

# result = storeInventory()
# print("Products With Stock Less Than 10 Units:", result)