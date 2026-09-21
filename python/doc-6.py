# # Q1. ATM Withdrawal

# def atmWithdrawal():
#     balance = float(input("Enter Account Balance: "))
#     withdrawal = float(input("Enter Withdrawal Amount: "))

#     if balance >= withdrawal:
#         if withdrawal % 100 == 0:
#             print("Withdrawal Successful")
#         else:
#             print("Enter amount in multiples of 100")
#     else:
#         print("Insufficient Balance")

# atmWithdrawal()


# # Q2. Online Shopping Discount

# def onlineShopping():
#     amount = float(input("Enter Purchase Amount: "))
#     premium = input("Premium Member (True/False): ")

#     if amount > 1000:
#         if premium.lower() == "true":
#             print("20% Discount Applied")
#         else:
#             print("10% Discount Applied")
#     else:
#         print("No Discount")

# onlineShopping()


# # Q3. College Admission

# def collegeAdmission():
#     marks = float(input("Enter Marks: "))
#     age = int(input("Enter Age: "))

#     if marks >= 60:
#         if age >= 17:
#             print("Admission Approved")
#         else:
#             print("Age Not Eligible")
#     else:
#         print("Marks Not Eligible")

# collegeAdmission()


# # Q4. Login System

# def loginSystem():
#     username = input("Enter Username: ")
#     password = input("Enter Password: ")

#     if username == "admin":
#         if password == "admin123":
#             print("Login Successful")
#         else:
#             print("Incorrect Password")
#     else:
#         print("Invalid Username")

# loginSystem()


# # Q5. Movie Booking

# def movieBooking():
#     age = int(input("Enter Age: "))
#     seats = input("Seats Available (True/False): ")

#     if age >= 18:
#         if seats.lower() == "true":
#             print("Booking Successful")
#         else:
#             print("House Full")
#     else:
#         print("Not Eligible")

# movieBooking()


# # Q6. Library Membership

# def libraryMembership():
#     member = input("Member (True/False): ")
#     overdue = int(input("Overdue Books: "))

#     if member.lower() == "true":
#         if overdue == 0:
#             print("Book Issued")
#         else:
#             print("Pay Fine First")
#     else:
#         print("Register First")

# libraryMembership()


# # Q7. Hospital Appointment

# def hospitalAppointment():
#     appointment = input("Appointment Booked (True/False): ")
#     doctor = input("Doctor Available (True/False): ")

#     if appointment.lower() == "true":
#         if doctor.lower() == "true":
#             print("Consultation Started")
#         else:
#             print("Please Wait")
#     else:
#         print("Book an Appointment First")

# hospitalAppointment()


# # Q8. Flight Boarding

# def flightBoarding():
#     passport = input("Passport Available (True/False): ")
#     ticket = input("Ticket Confirmed (True/False): ")

#     if passport.lower() == "true":
#         if ticket.lower() == "true":
#             print("Boarding Allowed")
#         else:
#             print("Ticket Not Confirmed")
#     else:
#         print("Passport Required")

# flightBoarding()


# # Q9. Driving License

# def drivingLicense():
#     age = int(input("Enter Age: "))
#     test = input("Learner Test Passed (True/False): ")

#     if age >= 18:
#         if test.lower() == "true":
#             print("License Issued")
#         else:
#             print("Retake Learner's Test")
#     else:
#         print("Underage")

# drivingLicense()


# # Q10. Hotel Check-in

# def hotelCheckIn():
#     booking = input("Booking Available (True/False): ")
#     idProof = input("ID Proof Available (True/False): ")

#     if booking.lower() == "true":
#         if idProof.lower() == "true":
#             print("Check-in Successful")
#         else:
#             print("ID Proof Required")
#     else:
#         print("Booking Not Found")

# hotelCheckIn()


# # Q11. Cricket Team Selection

# def cricketTeam():
#     runs = int(input("Enter Runs Scored: "))
#     fitness = input("Fitness Test Passed (True/False): ")

#     if runs >= 50:
#         if fitness.lower() == "true":
#             print("Player Selected")
#         else:
#             print("Fitness Test Failed")
#     else:
#         print("Not Selected")

# cricketTeam()


# # Q12. Employee Promotion

# def employeePromotion():
#     experience = int(input("Enter Years of Experience: "))
#     rating = float(input("Enter Performance Rating: "))

#     if experience >= 5:
#         if rating >= 8:
#             print("Promotion Approved")
#         else:
#             print("Promotion Delayed")
#     else:
#         print("Insufficient Experience")

# employeePromotion()


# # Q13. Scholarship Eligibility

# def scholarshipEligibility():
#     percentage = float(input("Enter Percentage: "))
#     income = float(input("Enter Annual Family Income: "))

#     if percentage >= 85:
#         if income < 300000:
#             print("Scholarship Approved")
#         else:
#             print("Income Exceeds Limit")
#     else:
#         print("Insufficient Marks")

# scholarshipEligibility()


# # Q14. Mobile Recharge

# def mobileRecharge():
#     amount = float(input("Enter Recharge Amount: "))
#     payment = input("Payment Successful (True/False): ")

#     if amount >= 199:
#         if payment.lower() == "true":
#             print("Recharge Successful")
#         else:
#             print("Payment Failed")
#     else:
#         print("Minimum Recharge Required")

# mobileRecharge()


# # Q15. Food Delivery

# def foodDelivery():
#     restaurant = input("Restaurant Open (True/False): ")
#     partner = input("Delivery Partner Available (True/False): ")

#     if restaurant.lower() == "true":
#         if partner.lower() == "true":
#             print("Order Accepted")
#         else:
#             print("No Delivery Partner Available")
#     else:
#         print("Restaurant Closed")

# foodDelivery()


# # Q16. Train Reservation

# def trainReservation():
#     seats = input("Seats Available (True/False): ")
#     payment = input("Payment Completed (True/False): ")

#     if seats.lower() == "true":
#         if payment.lower() == "true":
#             print("Ticket Confirmed")
#         else:
#             print("Complete Payment First")
#     else:
#         print("Waiting List")

# trainReservation()


# # Q17. Online Exam

# def onlineExam():
#     internet = input("Internet Available (True/False): ")
#     webcam = input("Webcam Enabled (True/False): ")

#     if internet.lower() == "true":
#         if webcam.lower() == "true":
#             print("Exam Started")
#         else:
#             print("Enable Webcam")
#     else:
#         print("Connect to the Internet")

# onlineExam()


# # Q18. Bike Rental

# def bikeRental():
#     licenseStatus = input("Driving License (True/False): ")
#     bike = input("Bike Available (True/False): ")

#     if licenseStatus.lower() == "true":
#         if bike.lower() == "true":
#             print("Bike Rental Approved")
#         else:
#             print("No Bikes Available")
#     else:
#         print("Driving License Required")

# bikeRental()


# # Q19. Bank Loan

# def bankLoan():
#     salary = float(input("Enter Monthly Salary: "))
#     credit = int(input("Enter Credit Score: "))

#     if salary >= 30000:
#         if credit >= 700:
#             print("Loan Approved")
#         else:
#             print("Poor Credit Score")
#     else:
#         print("Salary Too Low")

# bankLoan()


# # Q20. Cinema Entry

# def cinemaEntry():
#     ticket = input("Ticket Available (True/False): ")
#     valid = input("Ticket Valid (True/False): ")

#     if ticket.lower() == "true":
#         if valid.lower() == "true":
#             print("Entry Allowed")
#         else:
#             print("Invalid Ticket")
#     else:
#         print("Buy a Ticket First")

# cinemaEntry()


# # Q21. Gym Admission

# def gymAdmission():
#     age = int(input("Enter Age: "))
#     certificate = input("Medical Certificate (True/False): ")

#     if age >= 18:
#         if certificate.lower() == "true":
#             print("Gym Admission Approved")
#         else:
#             print("Medical Certificate Required")
#     else:
#         print("Not Eligible for Gym Admission")

# gymAdmission()


# # Q22. Company Interview

# def companyInterview():
#     degree = input("Degree Completed (True/False): ")
#     aptitude = input("Aptitude Test Passed (True/False): ")

#     if degree.lower() == "true":
#         if aptitude.lower() == "true":
#             print("Interview Scheduled")
#         else:
#             print("Aptitude Test Failed")
#     else:
#         print("Degree Required")

# companyInterview()


# # Q23. Courier Service

# def courierService():
#     weight = float(input("Enter Parcel Weight: "))
#     address = input("Address Serviceable (True/False): ")

#     if weight <= 20:
#         if address.lower() == "true":
#             print("Parcel Accepted")
#         else:
#             print("Delivery Area Not Serviceable")
#     else:
#         print("Parcel Exceeds Weight Limit")

# courierService()


# # Q24. Water Supply

# def waterSupply():
#     level = float(input("Enter Water Level: "))
#     motor = input("Motor Working (True/False): ")

#     if level < 20:
#         if motor.lower() == "true":
#             print("Filling Water Tank")
#         else:
#             print("Repair the Motor")
#     else:
#         print("Water Level is Sufficient")

# waterSupply()


# # Q25. Smart Door Lock

# def smartDoorLock():
#     fingerprint = input("Fingerprint Match (True/False): ")
#     pin = input("PIN Correct (True/False): ")

#     if fingerprint.lower() == "true":
#         if pin.lower() == "true":
#             print("Door Unlocked")
#         else:
#             print("Incorrect PIN")
#     else:
#         print("Fingerprint Not Recognized")

# smartDoorLock()


# # Q26. Laptop Purchase EMI

# def laptopEMI():
#     price = float(input("Enter Laptop Price: "))
#     emi = input("EMI Selected (True/False): ")

#     if price > 50000:
#         if emi.lower() == "true":
#             print("EMI Approved")
#         else:
#             print("Pay Full Amount")
#     else:
#         print("EMI Not Available for This Price")

# laptopEMI()


# # Q27. School Bus Service

# def schoolBus():
#     fees = input("Fees Paid (True/False): ")
#     busPass = input("Bus Pass Available (True/False): ")

#     if fees.lower() == "true":
#         if busPass.lower() == "true":
#             print("Boarding Allowed")
#         else:
#             print("Collect Bus Pass")
#     else:
#         print("Pay School Fees First")

# schoolBus()


# # Q28. Petrol Pump

# def petrolPump():
#     fuel = input("Fuel Available (True/False): ")
#     payment = input("Payment Successful (True/False): ")

#     if fuel.lower() == "true":
#         if payment.lower() == "true":
#             print("Fuel Filled Successfully")
#         else:
#             print("Payment Failed")
#     else:
#         print("Fuel Not Available")

# petrolPump()


# # Q29. Warehouse Entry

# def warehouseEntry():
#     idCard = input("ID Card Available (True/False): ")
#     fingerprint = input("Fingerprint Verified (True/False): ")

#     if idCard.lower() == "true":
#         if fingerprint.lower() == "true":
#             print("Entry Allowed")
#         else:
#             print("Fingerprint Verification Failed")
#     else:
#         print("ID Card Required")

# warehouseEntry()


# # Q30. Software Installation

# def softwareInstallation():
#     operatingSystem = input("Operating System Compatible (True/False): ")
#     storage = float(input("Available Storage: "))

#     if operatingSystem.lower() == "true":
#         if storage >= 20:
#             print("Software Installed Successfully")
#         else:
#             print("Insufficient Storage")
#     else:
#         print("Operating System Not Supported")

# softwareInstallation()