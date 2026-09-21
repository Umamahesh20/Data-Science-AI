# # Q1. Student Grade

# def studentGrade():
#     marks = int(input("Enter marks: "))

#     if marks >= 90:
#         print("Grade A")
#     elif marks >= 75:
#         print("Grade B")
#     elif marks >= 60:
#         print("Grade C")
#     elif marks >= 35:
#         print("Grade D")
#     else:
#         print("Fail")

# studentGrade()


# # Q2. Traffic Signal

# def trafficSignal():
#     signal = input("Enter traffic signal color: ")

#     if signal.lower() == "red":
#         print("Stop")
#     elif signal.lower() == "yellow":
#         print("Get Ready")
#     elif signal.lower() == "green":
#         print("Go")
#     else:
#         print("Invalid Signal")

# trafficSignal()


# # Q3. Movie Ticket Price

# def movieTicket():
#     age = int(input("Enter age: "))

#     if age < 5:
#         print("Ticket Price: Free")
#     elif age <= 17:
#         print("Ticket Price: ₹100")
#     elif age <= 59:
#         print("Ticket Price: ₹200")
#     else:
#         print("Ticket Price: ₹120")

# movieTicket()


# # Q4. Electricity Bill Category

# def electricityCategory():
#     units = int(input("Enter units consumed: "))

#     if units <= 100:
#         print("Domestic")
#     elif units <= 300:
#         print("Standard")
#     elif units <= 500:
#         print("Premium")
#     else:
#         print("Heavy User")

# electricityCategory()


# # Q5. Bank Loan Eligibility

# def loanEligibility():
#     credit = int(input("Enter credit score: "))

#     if credit >= 750:
#         print("Excellent")
#     elif credit >= 650:
#         print("Good")
#     elif credit >= 550:
#         print("Average")
#     else:
#         print("Not Eligible")

# loanEligibility()


# # Q6. BMI Category

# def bmiCategory():
#     bmi = float(input("Enter BMI: "))

#     if bmi < 18.5:
#         print("Underweight")
#     elif bmi < 25:
#         print("Normal")
#     elif bmi < 30:
#         print("Overweight")
#     else:
#         print("Obese")

# bmiCategory()


# # Q7. Internet Speed Rating

# def internetSpeed():
#     speed = float(input("Enter internet speed in Mbps: "))

#     if speed < 10:
#         print("Slow")
#     elif speed <= 50:
#         print("Average")
#     elif speed <= 100:
#         print("Fast")
#     else:
#         print("Very Fast")

# internetSpeed()


# # Q8. Restaurant Feedback

# def restaurantFeedback():
#     rating = int(input("Enter rating (1-5): "))

#     if rating == 5:
#         print("Excellent")
#     elif rating == 4:
#         print("Very Good")
#     elif rating == 3:
#         print("Good")
#     elif rating == 2:
#         print("Average")
#     elif rating == 1:
#         print("Poor")
#     else:
#         print("Invalid Rating")

# restaurantFeedback()


# # Q9. Cricket Score

# def cricketScore():
#     runs = int(input("Enter runs: "))

#     if runs == 0:
#         print("Duck")
#     elif runs < 50:
#         print("Good")
#     elif runs < 100:
#         print("Half Century")
#     else:
#         print("Century")

# cricketScore()


# # Q10. Attendance Status

# def attendanceStatus():
#     attendance = float(input("Enter attendance percentage: "))

#     if attendance >= 90:
#         print("Excellent")
#     elif attendance >= 75:
#         print("Eligible")
#     elif attendance >= 60:
#         print("Warning")
#     else:
#         print("Not Eligible")

# attendanceStatus()


# # Q11. Courier Weight Charge

# def courierWeight():
#     weight = float(input("Enter parcel weight: "))

#     if weight <= 5:
#         print("Light Parcel")
#     elif weight <= 10:
#         print("Medium Parcel")
#     else:
#         print("Heavy Parcel")

# courierWeight()


# # Q12. Mobile Battery Status

# def batteryStatus():
#     battery = float(input("Enter battery percentage: "))

#     if battery < 20:
#         print("Low Battery")
#     elif battery <= 50:
#         print("Medium Battery")
#     else:
#         print("High Battery")

# batteryStatus()


# # Q13. Air Conditioner Mode

# def acMode():
#     temperature = float(input("Enter room temperature: "))

#     if temperature < 20:
#         print("Fan Mode")
#     elif temperature <= 30:
#         print("Normal Mode")
#     else:
#         print("Cooling Mode")

# acMode()


# # Q14. Rainfall Level

# def rainfallLevel():
#     rainfall = float(input("Enter rainfall in mm: "))

#     if rainfall < 10:
#         print("Light Rain")
#     elif rainfall <= 50:
#         print("Moderate Rain")
#     else:
#         print("Heavy Rain")

# rainfallLevel()


# # Q15. Water Tank Status

# def waterTank():
#     level = float(input("Enter water level percentage: "))

#     if level < 20:
#         print("Low")
#     elif level < 80:
#         print("Medium")
#     else:
#         print("Full")

# waterTank()


# # Q16. Exam Rank

# def examRank():
#     marks = int(input("Enter marks: "))

#     if marks >= 75:
#         print("First Class")
#     elif marks >= 60:
#         print("Second Class")
#     elif marks >= 35:
#         print("Third Class")
#     else:
#         print("Fail")

# examRank()


# # Q17. Salary Tax Slab

# def salaryTax():
#     salary = float(input("Enter annual salary: "))

#     if salary <= 300000:
#         print("Low Tax Slab")
#     elif salary <= 700000:
#         print("Medium Tax Slab")
#     else:
#         print("High Tax Slab")

# salaryTax()


# # Q18. Hotel Room Type

# def hotelRoom():
#     budget = float(input("Enter budget: "))

#     if budget < 2000:
#         print("Standard Room")
#     elif budget <= 5000:
#         print("Deluxe Room")
#     else:
#         print("Suite Room")

# hotelRoom()


# # Q19. Vehicle Speed Warning

# def vehicleSpeed():
#     speed = float(input("Enter vehicle speed: "))

#     if speed <= 60:
#         print("Safe Speed")
#     elif speed <= 80:
#         print("Speed Warning")
#     else:
#         print("Overspeed")

# vehicleSpeed()


# # Q20. Employee Performance

# def employeePerformance():
#     score = float(input("Enter performance score: "))

#     if score >= 90:
#         print("Outstanding")
#     elif score >= 75:
#         print("Excellent")
#     elif score >= 60:
#         print("Good")
#     elif score >= 35:
#         print("Average")
#     else:
#         print("Poor")

# employeePerformance()


# # Q21. Online Shopping Discount

# def shoppingDiscount():
#     amount = float(input("Enter purchase amount: "))

#     if amount >= 5000:
#         print("15% Discount")
#     elif amount >= 3000:
#         print("10% Discount")
#     elif amount >= 1000:
#         print("5% Discount")
#     else:
#         print("No Discount")

# shoppingDiscount()


# # Q22. Data Usage Alert

# def dataUsage():
#     data = float(input("Enter data usage in GB: "))

#     if data < 50:
#         print("Low Usage")
#     elif data <= 80:
#         print("Normal Usage")
#     else:
#         print("High Usage")

# dataUsage()


# # Q23. Fuel Level Indicator

# def fuelLevel():
#     fuel = float(input("Enter fuel percentage: "))

#     if fuel < 20:
#         print("Low Fuel")
#     elif fuel <= 50:
#         print("Medium Fuel")
#     else:
#         print("High Fuel")

# fuelLevel()


# # Q24. ATM Cash Withdrawal

# def atmCashWithdrawal():
#     amount = float(input("Enter withdrawal amount: "))

#     if amount <= 5000:
#         print("Small Withdrawal")
#     elif amount <= 10000:
#         print("Medium Withdrawal")
#     else:
#         print("Large Withdrawal")

# atmCashWithdrawal()


# # Q25. Library Fine

# def libraryFine():
#     days = int(input("Enter overdue days: "))

#     if days <= 3:
#         print("Low Fine")
#     elif days <= 7:
#         print("Medium Fine")
#     else:
#         print("High Fine")

# libraryFine()


# # Q26. Delivery Priority

# def deliveryPriority():
#     weight = float(input("Enter parcel weight: "))

#     if weight <= 5:
#         print("Express Delivery")
#     elif weight <= 15:
#         print("Standard Delivery")
#     else:
#         print("Heavy Delivery")

# deliveryPriority()


# # Q27. Internet Data Plan

# def internetDataPlan():
#     data = float(input("Enter monthly data usage: "))

#     if data <= 50:
#         print("Basic Plan")
#     elif data <= 150:
#         print("Standard Plan")
#     else:
#         print("Premium Plan")

# internetDataPlan()


# # Q28. Hospital Emergency Level

# def emergencyLevel():
#     priority = int(input("Enter priority level (1-4): "))

#     if priority == 1:
#         print("Critical Priority")
#     elif priority == 2:
#         print("High Priority")
#     elif priority == 3:
#         print("Medium Priority")
#     elif priority == 4:
#         print("Low Priority")
#     else:
#         print("Invalid Priority")

# emergencyLevel()


# # Q29. Hotel Star Rating

# def hotelRating():
#     rating = int(input("Enter hotel rating (1-5): "))

#     if rating == 5:
#         print("Excellent Hotel")
#     elif rating == 4:
#         print("Very Good Hotel")
#     elif rating == 3:
#         print("Good Hotel")
#     elif rating == 2:
#         print("Average Hotel")
#     elif rating == 1:
#         print("Poor Hotel")
#     else:
#         print("Invalid Rating")

# hotelRating()


# # Q30. E-commerce Membership

# def ecommerceMembership():
#     amount = float(input("Enter yearly purchase amount: "))

#     if amount >= 100000:
#         print("Gold Membership")
#     elif amount >= 50000:
#         print("Silver Membership")
#     elif amount >= 25000:
#         print("Bronze Membership")
#     else:
#         print("Basic Membership")

# ecommerceMembership()