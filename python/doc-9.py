# # # 1. ATM Withdrawal Validation
# # # Concept: while-else
# # # Task: Check whether the requested amount can be formed using available note denominations.
# # def checkWithdrawal(notes, amount):
# #     i = 0
# #     while i < len(notes):
# #         if amount % notes[i] == 0:
# #             return True
# #         i += 1
# #     else:
# #         return False

# # n = int(input("Enter number of notes: "))
# # notes = list(map(int, input("Enter note denominations: ").replace(",", " ").split()))
# # amount = int(input("Enter withdrawal amount: "))

# # if checkWithdrawal(notes, amount):
# #     print("Withdrawal can be processed")
# # else:
# #     print("Withdrawal cannot be processed")

# # # 2. Detect Fraud Transaction
# # # Task: If any transaction crosses the fraud limit, stop checking.
# # def checkFraud(transactions, limit):
# #     i = 0
# #     while i < len(transactions):
# #         if transactions[i] > limit:
# #             print("Suspicious transaction detected")
# #             break
# #         i += 1
# #     else:
# #         print("No suspicious transaction")

# # n = int(input("Enter number of transactions: "))
# # transactions = list(map(int, input("Enter transactions: ").replace(",", " ").split()))
# # limit = int(input("Enter fraud limit: "))
# # checkFraud(transactions, limit)

# # # 3. Validate Student Marks Entry
# # # Task: Check whether all marks are valid from 0 to 100.
# # def validateMarks(marks):
# #     i = 0
# #     while i < len(marks):
# #         if marks[i] < 0 or marks[i] > 100:
# #             print("Invalid marks found")
# #             break
# #         i += 1
# #     else:
# #         print("All marks are valid")

# # n = int(input("Enter number of students: "))
# # marks = list(map(int, input("Enter marks: ").replace(",", " ").split()))
# # validateMarks(marks)

# # # 4. Find Available Parking Slot
# # # 0 = empty
# # # 1 = occupied
# # def checkParking(slots):
# #     i = 0
# #     while i < len(slots):
# #         if slots[i] == 0:
# #             print("Parking slot available")
# #             break
# #         i += 1
# #     else:
# #         print("No parking slot available")

# # n = int(input("Enter number of parking slots: "))
# # slots = list(map(int, input("Enter slot status: ").replace(",", " ").split()))
# # checkParking(slots)

# # # 5. Check Product Quality
# # # Task: If any product score is below minimum quality level, reject the batch.
# # def checkQuality(scores, minimum):
# #     i = 0
# #     while i < len(scores):
# #         if scores[i] < minimum:
# #             print("Quality check failed")
# #             break
# #         i += 1
# #     else:
# #         print("Quality check passed")

# # n = int(input("Enter number of products: "))
# # scores = list(map(int, input("Enter quality scores: ").replace(",", " ").split()))
# # minimum = int(input("Enter minimum quality level: "))
# # checkQuality(scores, minimum)

# # # 6. Verify Password Rules
# # # Task: Check whether password contains at least one uppercase letter.
# # def verifyPassword(password):
# #     i = 0
# #     while i < len(password):
# #         if password[i].isupper():
# #             print("Password contains uppercase letter")
# #             break
# #         i += 1
# #     else:
# #         print("Password does not contain uppercase letter")

# # password = input("Enter password: ")
# # verifyPassword(password)

# # # 7. Find Available Doctor Appointment
# # # 1 = booked
# # # 0 = available
# # def checkAppointment(slots):
# #     i = 0
# #     while i < len(slots):
# #         if slots[i] == 0:
# #             print("Appointment available")
# #             break
# #         i += 1
# #     else:
# #         print("No appointment available")

# # n = int(input("Enter number of slots: "))
# # slots = list(map(int, input("Enter slot status: ").replace(",", " ").split()))
# # checkAppointment(slots)

# # # 8. Detect Damaged Packages
# # # Task: Weight less than 1 kg means damaged.
# # def checkPackages(weights):
# #     i = 0
# #     while i < len(weights):
# #         if weights[i] < 1:
# #             print("Damaged package found")
# #             break
# #         i += 1
# #     else:
# #         print("All packages are good")

# # n = int(input("Enter number of packages: "))
# # weights = list(map(float, input("Enter package weights: ").replace(",", " ").split()))
# # checkPackages(weights)
# # 9. Check Password Attempts History
# # 1 = success
# # 0 = failure

# def checkLogin(attempts):
#     i = 0
#     while i < len(attempts):
#         if attempts[i] == 1:
#             print("Successful login found")
#             break
#         i += 1
#     else:
#         print("No successful login found")

# n = int(input("Enter number of attempts: "))
# attempts = []
# i = 0
# while i < n:
#     status = int(input("Enter attempt status (1 = success, 0 = failure): "))
#     if status == 0 or status == 1:
#         attempts.append(status)
#         i += 1
#     else:
#         print("Please enter only 0 or 1")
# checkLogin(attempts)

# # 10. Check Library Book Condition
# # 0 = good
# # 1 = damaged
# def checkBooks(books):
#     i = 0
#     while i < len(books):
#         if books[i] == 1:
#             print("Damaged book detected")
#             break
#         i += 1
#     else:
#         print("All books are in good condition")

# n = int(input("Enter number of books: "))
# books = list(map(int, input("Enter book status: ").replace(",", " ").split()))
# checkBooks(books)

# # 11. Find Nearest Charging Station
# # Task: Check whether a station exists within 5 km.
# def checkChargingStation(distances):
#     i = 0
#     while i < len(distances):
#         if distances[i] <= 5:
#             print("Charging station found")
#             break
#         i += 1
#     else:
#         print("No charging station within 5 km")

# n = int(input("Enter number of stations: "))
# distances = list(map(int, input("Enter distances: ").replace(",", " ").split()))
# checkChargingStation(distances)

# # 12. Check Website Server Status
# # 1 = active
# # 0 = down
# def checkServers(servers):
#     i = 0
#     while i < len(servers):
#         if servers[i] == 1:
#             print("Active server found")
#             break
#         i += 1
#     else:
#         print("No active server found")

# n = int(input("Enter number of servers: "))
# servers = list(map(int, input("Enter server status: ").replace(",", " ").split()))
# checkServers(servers)

# # 13. Verify Attendance Records
# # Task: If any attendance is below 75%, stop checking.
# def checkAttendance(attendance, minimum):
#     i = 0
#     while i < len(attendance):
#         if attendance[i] < minimum:
#             print("Attendance shortage detected")
#             break
#         i += 1
#     else:
#         print("Attendance is satisfactory")

# n = int(input("Enter number of students: "))
# attendance = list(map(int, input("Enter attendance percentages: ").replace(",", " ").split()))
# minimum = int(input("Enter minimum attendance: "))
# checkAttendance(attendance, minimum)

# # 14. Detect Duplicate Booking
# # Task: If duplicate booking ID appears, stop.
# def checkDuplicate(bookings):
#     i = 0
#     while i < len(bookings):
#         j = i + 1
#         while j < len(bookings):
#             if bookings[i] == bookings[j]:
#                 print("Duplicate booking found")
#                 return
#             j += 1
#         i += 1
#     else:
#         print("No duplicate booking found")

# n = int(input("Enter number of bookings: "))
# bookings = list(map(int, input("Enter booking IDs: ").replace(",", " ").split()))
# checkDuplicate(bookings)

# # 15. Check Security Access Cards
# # 1 = valid
# # 0 = expired
# def checkCards(cards):
#     i = 0
#     while i < len(cards):
#         if cards[i] == 0:
#             print("Expired card detected")
#             break
#         i += 1
#     else:
#         print("All access cards are valid")

# n = int(input("Enter number of cards: "))
# cards = list(map(int, input("Enter card status: ").replace(",", " ").split()))
# checkCards(cards)

# # 16. ATM PIN Verification System
# # Concept: while-else
# # Task: Allow 3 attempts to enter the correct PIN.
# def verifyPIN(correctPin, attempts):
#     count = 0
#     while count < attempts:
#         pin = int(input("Enter PIN: "))
#         if pin == correctPin:
#             print("PIN verified successfully")
#             break
#         count += 1
#     else:
#         print("Account blocked")

# correctPin = int(input("Enter correct PIN: "))
# attempts = int(input("Enter maximum attempts: "))
# verifyPIN(correctPin, attempts)

# # 17. Online Payment Retry System
# # 1 = success
# # 0 = failure
# def paymentRetry(attempts):
#     count = 0
#     while count < attempts:
#         status = int(input("Enter payment status (1/0): "))
#         if status == 1:
#             print("Payment successful")
#             break
#         count += 1
#     else:
#         print("Payment failed after retries")

# attempts = int(input("Enter maximum attempts: "))
# paymentRetry(attempts)

# # 18. OTP Verification
# # Task: Allow user 3 attempts to enter correct OTP.
# def verifyOTP(correctOTP):
#     count = 0
#     while count < 3:
#         otp = int(input("Enter OTP: "))
#         if otp == correctOTP:
#             print("OTP verified successfully")
#             break
#         count += 1
#     else:
#         print("OTP verification failed")

# correctOTP = int(input("Enter correct OTP: "))
# verifyOTP(correctOTP)

# # 19. File Download Retry
# # 1 = download success
# # 0 = failed
# def downloadFile(attempts):
#     count = 0
#     while count < attempts:
#         status = int(input("Enter download status (1/0): "))
#         if status == 1:
#             print("File downloaded successfully")
#             break
#         count += 1
#     else:
#         print("File download failed")

# attempts = int(input("Enter maximum attempts: "))
# downloadFile(attempts)

# # 20. Game Life System
# # Task: Player gets 3 chances.
# # 1 = life lost
# def gameLife(lives):
#     count = 0
#     while count < lives:
#         status = int(input("Enter 1 if life is lost: "))
#         if status == 1:
#             count += 1
#     else:
#         print("Game over")

# lives = int(input("Enter number of lives: "))
# gameLife(lives)

# # 21. Battery Charging System
# # Task: Increase battery by 10% until it reaches 100%.
# def chargeBattery(battery):
#     while battery < 100:
#         battery += 10
#         print("Battery:", battery, "%")
#     else:
#         print("Battery fully charged")

# battery = int(input("Enter current battery percentage: "))
# chargeBattery(battery)

# # 22. Elevator Movement System
# # Task: Move elevator floor by floor until destination.
# def moveElevator(current, destination):
#     while current != destination:
#         if current < destination:
#             current += 1
#         else:
#             current -= 1
#         print("Current floor:", current)
#     else:
#         print("Reached destination floor")

# current = int(input("Enter current floor: "))
# destination = int(input("Enter destination floor: "))
# moveElevator(current, destination)

# # 23. Traffic Signal Countdown
# # Task: Decrease signal timer until it reaches zero.
# def signalCountdown(timer):
#     while timer > 0:
#         print("Time remaining:", timer)
#         timer -= 1
#     else:
#         print("Signal changed")

# timer = int(input("Enter signal timer: "))
# signalCountdown(timer)

# # 24. Server Restart System
# # 1 = started
# # 0 = failed
# def restartServer(attempts):
#     count = 0
#     while count < attempts:
#         status = int(input("Enter server status (1/0): "))
#         if status == 1:
#             print("Server started successfully")
#             break
#         count += 1
#     else:
#         print("Server restart failed")

# attempts = int(input("Enter number of restart attempts: "))
# restartServer(attempts)

# # 25. Food Delivery Tracking
# # 0 = not delivered
# # 1 = delivered
# def trackDelivery(attempts):
#     count = 0
#     while count < attempts:
#         status = int(input("Enter delivery status (1/0): "))
#         if status == 1:
#             print("Order delivered")
#             break
#         count += 1
#     else:
#         print("Order not delivered")

# attempts = int(input("Enter number of status checks: "))
# trackDelivery(attempts)

# # 26. Internet Connection Retry
# # 1 = connected
# # 0 = failed
# def internetConnection(attempts):
#     count = 0
#     while count < attempts:
#         status = int(input("Enter connection status (1/0): "))
#         if status == 1:
#             print("Internet connected")
#             break
#         count += 1
#     else:
#         print("Unable to connect")

# attempts = int(input("Enter number of attempts: "))
# internetConnection(attempts)

# # 27. Password Reset Verification
# # 1 = verified
# # 0 = failed
# def verifyIdentity(attempts):
#     count = 0
#     while count < attempts:
#         status = int(input("Enter verification status (1/0): "))
#         if status == 1:
#             print("Identity verified")
#             break
#         count += 1
#     else:
#         print("Identity verification failed")

# attempts = int(input("Enter number of attempts: "))
# verifyIdentity(attempts)

# # 28. Washing Machine Cycle
# # Task: Reduce remaining time until washing completes.
# def washingMachine(time):
#     while time > 0:
#         print("Remaining time:", time, "minutes")
#         time -= 1
#     else:
#         print("Washing completed")

# time = int(input("Enter remaining washing time: "))
# washingMachine(time)

# # 29. Inventory Restocking System
# # Task: Increase stock until required stock level is reached.
# def restock(current, required):
#     while current < required:
#         current += 10
#         print("Current stock:", current)
#     else:
#         print("Stock requirement completed")

# current = int(input("Enter current stock: "))
# required = int(input("Enter required stock: "))
# restock(current, required)

# # 30. Bank Transaction Processing Queue
# # 1 = completed
# # 0 = failed
# def processTransactions(total):
#     count = 0
#     while count < total:
#         status = int(input("Enter transaction status (1/0): "))
#         if status == 0:
#             print("Transaction failed")
#             return
#         count += 1
#     else:
#         print("All transactions processed")

# total = int(input("Enter number of transactions: "))
# processTransactions(total)