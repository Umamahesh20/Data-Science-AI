# # 1. Smart Password Validator 
# # Concept: Function with string parameter and boolean return 
# # Task: Create a function validatePassword(password) that checks 
# # whether a password: 
# # Has at least 8 characters 
# # Contains at least one digit 
# # Contains at least one uppercase letter 
# # Example Input: 
# # password = 'Python123' 
# # Example Output: 
# # Valid Password

# # def validatePassword(password):
# #     if len(password)<8:
# #         return False
# #     if not any(char.isdigit() for char in password):
# #         return False
# #     if not any(char.isupper() for char in password):
# #         return False
# #     return True
# # password = 'Umamahesh123'
# # if validatePassword(password):
# #     print("Valid Password")
# # else:
# #     print("Invalid Password")

# # 2. Digital Wallet Balance Checker 
# # Concept: Function with multiple parameters Task: Create a 
# # function checkBalance(balance, withdrawal) that returns whether 
# # the withdrawal is possible. 
# # Example Input: 
# # balance = 5000 
# # withdrawal = 3000 
# # Example Output: 
# # Transaction Approved 
# # # Remaining Balance: 2000 

# # def checkBalance(balance, withdrawal):
# #     if withdrawal<=balance:
# #         return True
# #     else:
# #         return False

# # balance = float(input("Enter your balance: "))
# # withdrawal = float(input("Enter withdrawal amount: "))

# # if checkBalance(balance, withdrawal):
# #     print("Transaction Approved")
# #     print('Remaining Balance:', balance - withdrawal)
# # else:
# #     print("Transaction Not Approved")
# #     print('Remaining Balance:', balance)

# # 3. Temperature Converter 
# # Concept: Function returning calculated value Task: Create a 
# # function convertTemperature(celsius) to convert Celsius into 
# # Fahrenheit. 
# # Example Input: 
# # celsius = 35 
# # Example Output: 
# # 95 Fahrenheit 

# # def convertTemperature(celsius):
# #     fahrenheit = (celsius * 9 / 5) + 32
# #     return fahrenheit
# # celsius = float(input("Enter Temperture in Celsius:"))

# # result = convertTemperature(celsius)
# # print(result, "Fahrenheit")



# # 4. Employee Bonus Calculator 
# # Concept: Function with conditions Task: Create a function 
# # calculateBonus(salary, experience): 
# # Experience above 5 years → 20% bonus 
# # Otherwise → 10% bonus 
# # Example Input: 
# # salary = 50000 
# # experience = 7 
# # Example Output: 
# # Bonus = 10000 

# # def calculateBonus(salary, experience):
# #     if experience > 5:
# #         bonus = salary * 20 / 100
# #     else:
# #         bonus = salary * 10 / 100
# #     return bonus
# # salary= float(input('Enter the salary: '))
# # experience= float(input('Enter the experience: '))
# # bonus=calculateBonus(salary, experience)
# # print("Bonus =", int(bonus))

# # 5. ATM Note Counter 
# # Concept: Function with loops Task: Create a function 
# # countNotes(amount) that returns the number of 500, 200, and 100 
# # rupee notes required. 
# # Example Input: 
# # amount = 1800 
 
# # Example Output: 
# # 500 notes: 3 
# # 200 notes: 1 
# # 100 notes: 1

# # def countNotes(amount):
# #     notes500 = 0
# #     notes200 = 0
# #     notes100 = 0

# #     while amount >= 500:
# #         notes500 += 1
# #         amount -= 500

# #     while amount >= 200:
# #         notes200 += 1
# #         amount -= 200

# #     while amount >= 100:
# #         notes100 += 1
# #         amount -= 100

# #     return notes500, notes200, notes100


# # amount = int(input("Enter amount: "))

# # notes500, notes200, notes100 = countNotes(amount)

# # print("500 notes:", notes500)
# # print("200 notes:", notes200)
# # print("100 notes:", notes100)

# # 6. Movie Ticket Price Calculator 
# # Concept: Default arguments Task: Create a function 
# # ticketPrice(age, premium=False). 
# # Rules: 
# # Below 12 → ₹100 
# # Above 60 → ₹120 
# # Others → ₹200 
# # Premium adds ₹100 
# # Example Input: 
# # age = 25 
# # premium = True

# # def ticketPrice(age, premium=False):
# #     if age < 12:
# #         price = 100
# #     elif age > 60:
# #         price = 120
# #     else:
# #         price = 200

# #     if premium:
# #         price = price + 100

# #     return price


# # age = int(input("Enter your age: "))

# # premium_input = input("Is it a premium ticket? (True/False): ")

# # if premium_input == "True":
# #     premium = True
# # else:
# #     premium = False

# # price = ticketPrice(age, premium)

# # print("Ticket Price: ₹", price)    


# # 7. Student Grade Generator 
# # Concept: Function returning grade Task: Create a function 
# # findGrade(marks). 
# # Rules: 
# # 90+ → A 
# # 75-89 → B 
# # 50-74 → C 
# # Below 50 → Fail 
# # Example Input: 
# # marks = 82 
# # Example Output: 
# # Grade B 

# # def findGrade(marks):
# #     if marks >= 90:
# #         return "A"
# #     elif marks >= 75:
# #         return "B"
# #     elif marks >= 50:
# #         return "C"
# #     else:
# #         return "Fail"


# # marks = int(input("Enter marks: "))

# # grade = findGrade(marks)

# # print("Grade", grade)

# # 8. Username Generator
# # Concept: String manipulation function
# # Task: Create a function generateUsername(firstName, birthYear).
# # Example Input:
# # firstName = 'Ravi'
# # birthYear = 2002
# # Example Output:
# # ravi2002


# # def generateUsername(firstName, birthYear):
# #     return firstName.lower() + str(birthYear)


# # firstName = input("Enter first name: ")
# # birthYear = int(input("Enter birth year: "))

# # username = generateUsername(firstName, birthYear)

# # print("Username:", username)


# # 9. Electricity Usage Analyzer
# # Concept: Function returning multiple values
# # Task: Create a function calculateBill(units) that returns:
# # Total bill
# # Tax amount
# # Final amount
# #
# # Assumption:
# # First 100 units  -> ₹5/unit
# # Next 100 units   -> ₹7/unit
# # Above 200 units  -> ₹10/unit
# # Tax = 5% of total bill


# # def calculateBill(units):
# #     if units <= 100:
# #         totalBill = units * 5
# #     elif units <= 200:
# #         totalBill = (100 * 5) + ((units - 100) * 7)
# #     else:
# #         totalBill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

# #     taxAmount = totalBill * 5 / 100
# #     finalAmount = totalBill + taxAmount

# #     return totalBill, taxAmount, finalAmount


# # units = int(input("Enter electricity units: "))

# # totalBill, taxAmount, finalAmount = calculateBill(units)

# # print("Total Bill:", totalBill)
# # print("Tax Amount:", taxAmount)
# # print("Final Amount:", finalAmount)


# # 10. Password Strength Checker
# # Concept: Character checking
# # Task: Create a function checkStrength(password) that returns:
# # Weak
# # Medium
# # Strong
# #
# # Rules:
# # Weak   -> Less than 8 characters
# # Medium -> 8 or more characters with letters and digits
# # Strong -> 8 or more characters with uppercase, lowercase and digit


# # def checkStrength(password):
# #     hasUpper = False
# #     hasLower = False
# #     hasDigit = False

# #     for char in password:
# #         if char.isupper():
# #             hasUpper = True
# #         elif char.islower():
# #             hasLower = True
# #         elif char.isdigit():
# #             hasDigit = True

# #     if len(password) < 8:
# #         return "Weak"
# #     elif hasUpper and hasLower and hasDigit:
# #         return "Strong"
# #     else:
# #         return "Medium"


# # password = input("Enter password: ")

# # strength = checkStrength(password)

# # print("Password Strength:", strength)


# # 11. Number Frequency Counter
# # Concept: Function with list parameter
# # Task: Create a function countNumber(numbers, target) that
# # counts how many times a number appears.
# # Example Input:
# # numbers = [4,7,4,9,4]
# # target = 4
# # Output:
# # 4 appears 3 times


# # def countNumber(numbers, target):
# #     count = 0

# #     for number in numbers:
# #         if number == target:
# #             count += 1

# #     return count


# # numbers = list(map(int, input("Enter numbers : ").split()))
# # target = int(input("Enter target number: "))

# # result = countNumber(numbers, target)

# # print(target, "appears", result, "times")


# # 12. Remove Duplicate Values
# # Concept: Function returning modified list
# # Task: Create a function removeDuplicates(values) without
# # using set.
# # Example Input:
# # [5,2,5,8,2]
# # Output:
# # [5,2,8]


# # def removeDuplicates(values):
# #     result = []

# #     for value in values:
# #         if value not in result:
# #             result.append(value)

# #     return result


# # values = list(map(int, input("Enter values : ").split()))

# # result = removeDuplicates(values)

# # print("After removing duplicates:", result)


# # 13. Shopping Cart Discount
# # Concept: Function with list processing
# # Task: Create a function applyDiscount(prices):
# # Total above 5000 gets 15% discount
# # Otherwise 5%


# # def applyDiscount(prices):
# #     total = sum(prices)

# #     if total > 5000:
# #         discount = total * 15 / 100
# #     else:
# #         discount = total * 5 / 100

# #     finalAmount = total - discount

# #     return total, discount, finalAmount


# # prices = list(map(float, input("Enter prices : ").split()))

# # total, discount, finalAmount = applyDiscount(prices)

# # print("Total:", total)
# # print("Discount:", discount)
# # print("Final Amount:", finalAmount)


# # 14. Find Second Largest Number
# # Concept: Logic inside function
# # Task: Create a function secondLargest(numbers) without sorting.
# # Example Input:
# # [10,25,8,30]
# # Output:
# # 25


# # def secondLargest(numbers):
# #     largest = float('-inf')
# #     second = float('-inf')

# #     for number in numbers:
# #         if number > largest:
# #             second = largest
# #             largest = number
# #         elif number > second and number != largest:
# #             second = number

# #     return second


# # numbers = list(map(int, input("Enter numbers: ")))

# # result = secondLargest(numbers)

# # print("Second Largest:", result)

# # 15. Bank Loan Eligibility
# # Concept: Multiple condition function
# # Task: Create a function loanEligibility(income, age, creditScore).
# # Return:
# # Eligible
# # or
# # Not Eligible
# #
# # Rules:
# # Income >= 30000
# # Age between 21 and 60
# # Credit score >= 700


# # def loanEligibility(income, age, creditScore):
# #     if income >= 30000 and 21 <= age <= 60 and creditScore >= 700:
# #         return "Eligible"
# #     else:
# #         return "Not Eligible"


# # income = float(input("Enter monthly income: "))
# # age = int(input("Enter age: "))
# # creditScore = int(input("Enter credit score: "))

# # result = loanEligibility(income, age, creditScore)

# # print("Loan Status:", result)


# # 16. Email Validator
# # Concept: String validation
# # Task: Create a function validateEmail(email).
# # Check:
# # Contains @
# # Contains .
# # No spaces


# # def validateEmail(email):
# #     if "@" in email and "." in email and " " not in email:
# #         return True
# #     else:
# #         return False


# # email = input("Enter email: ")

# # if validateEmail(email):
# #     print("Valid Email")
# # else:
# #     print("Invalid Email")


# # 17. Password Generator
# # Concept: Function with random logic
# # Task: Create a function generatePassword(length) that creates
# # a password of given length.


# # import random
# # import string


# # def generatePassword(length):
# #     characters = string.ascii_letters + string.digits
# #     password = ""

# #     for i in range(length):
# #         password += random.choice(characters)

# #     return password


# # length = int(input("Enter password length: "))

# # password = generatePassword(length)

# # print("Generated Password:", password)


# # 18. Delivery Charge Calculator
# # Concept: Default parameter
# # Task: Create a function deliveryCharge(distance, express=False).
# # Rules:
# # Normal: ₹10/km
# # Express: ₹20/km


# # def deliveryCharge(distance, express=False):
# #     if express:
# #         return distance * 20
# #     else:
# #         return distance * 10


# # distance = float(input("Enter distance in km: "))
# # expressInput = input("Express delivery? (True/False): ")

# # if expressInput == "True":
# #     express = True
# # else:
# #     express = False

# # charge = deliveryCharge(distance, express)

# # print("Delivery Charge: ₹", charge)


# # 19. Library Fine Calculator
# # Concept: Date logic simulation
# # Task: Create a function calculateFine(daysLate).
# # Rules:
# # First 5 days -> ₹2/day
# # Next days -> ₹5/day


# # def calculateFine(daysLate):
# #     if daysLate <= 5:
# #         fine = daysLate * 2
# #     else:
# #         fine = (5 * 2) + ((daysLate - 5) * 5)

# #     return fine


# # daysLate = int(input("Enter number of days late: "))

# # fine = calculateFine(daysLate)

# # print("Library Fine: ", fine)


# # # 20. Attendance Percentage
# # # Concept: Mathematical function
# # # Task: Create a function attendancePercentage(totalDays, presentDays).


# # def attendancePercentage(totalDays, presentDays):
# #     percentage = (presentDays / totalDays) * 100
# #     return percentage


# # totalDays = int(input("Enter total working days: "))
# # presentDays = int(input("Enter present days: "))

# # percentage = attendancePercentage(totalDays, presentDays)

# # print("Attendance Percentage:", percentage, "%")


# # 21. Vehicle Speed Monitor
# # Concept: Function returning message
# # Task: Create a function checkSpeed(speed).
# # Rules:
# # Below 60 -> Normal
# # 60-100 -> Warning
# # Above 100 -> Over Speed


# # def checkSpeed(speed):
# #     if speed < 60:
# #         return "Normal"
# #     elif speed <= 100:
# #         return "Warning"
# #     else:
# #         return "Over Speed"


# # speed = float(input("Enter vehicle speed: "))

# # result = checkSpeed(speed)

# # print("Speed Status:", result)


# # 22. Grocery Inventory Checker
# # Concept: Dictionary parameter
# # Task: Create a function checkStock(items, product) that checks
# # availability.


# # def checkStock(items, product):
# #     if product in items and items[product] > 0:
# #         return True
# #     else:
# #         return False


# # items = {
# #     "rice": 10,
# #     "sugar": 5,
# #     "oil": 0,
# #     "milk": 8
# # }

# # product = input("Enter product name: ").lower()

# # if checkStock(items, product):
# #     print("Product Available")
# #     print("Quantity:", items[product])
# # else:
# #     print("Product Not Available")


# # 23. Word Analyzer
# # Concept: String + multiple return values
# # Task: Create a function analyzeWord(word) returning:
# # Number of characters
# # Number of vowels
# # Number of consonants


# # def analyzeWord(word):
# #     characters = len(word)
# #     vowels = 0
# #     consonants = 0

# #     for char in word.lower():
# #         if char.isalpha():
# #             if char in "aeiou":
# #                 vowels += 1
# #             else:
# #                 consonants += 1

# #     return characters, vowels, consonants


# # word = input("Enter a word: ")

# # characters, vowels, consonants = analyzeWord(word)

# # print("Number of characters:", characters)
# # print("Number of vowels:", vowels)
# # print("Number of consonants:", consonants)


# # 24. Train Ticket Fare Calculator
# # Concept: Multiple arguments
# # Task: Create a function calculateFare(age, distance, classType).
# #
# # Assumption:
# # General -> ₹2/km
# # Sleeper -> ₹3/km
# # AC       -> ₹5/km
# #
# # Children below 12 -> 50% fare
# # Senior citizens above 60 -> 30% discount


# # def calculateFare(age, distance, classType):
# #     if classType.lower() == "general":
# #         rate = 2
# #     elif classType.lower() == "sleeper":
# #         rate = 3
# #     elif classType.lower() == "ac":
# #         rate = 5
# #     else:
# #         return 0

# #     fare = distance * rate

# #     if age < 12:
# #         fare = fare * 50 / 100
# #     elif age > 60:
# #         fare = fare * 70 / 100

# #     return fare


# # age = int(input("Enter age: "))
# # distance = float(input("Enter distance in km: "))
# # classType = input("Enter class (General/Sleeper/AC): ")

# # fare = calculateFare(age, distance, classType)

# # print("Ticket Fare: ₹", fare)


# # 25. Mobile Data Usage Tracker
# # Concept: Function with calculations
# # Task: Create a function checkDataUsage(totalData, usedData).
# # Return remaining data percentage.


# # def checkDataUsage(totalData, usedData):
# #     remainingData = totalData - usedData
# #     remainingPercentage = (remainingData / totalData) * 100

# #     return remainingPercentage


# # totalData = float(input("Enter total data in GB: "))
# # usedData = float(input("Enter used data in GB: "))

# # percentage = checkDataUsage(totalData, usedData)

# # print("Remaining Data Percentage:", percentage, "%")



# # 26. Restaurant Bill Splitter
# # Concept: Function with multiple outputs
# # Task: Create a function splitBill(amount, people, tip).
# # Return:
# # Tip amount
# # Final bill
# # Each person's share


# # def splitBill(amount, people, tip):
# #     tipAmount = amount * tip / 100
# #     finalBill = amount + tipAmount
# #     share = finalBill / people

# #     return tipAmount, finalBill, share


# # amount = float(input("Enter bill amount: "))
# # people = int(input("Enter number of people: "))
# # tip = float(input("Enter tip percentage: "))

# # tipAmount, finalBill, share = splitBill(amount, people, tip)

# # print("Tip Amount:", tipAmount)
# # print("Final Bill:", finalBill)
# # print("Each Person's Share:", share)


# # 27. File Size Converter
# # Concept: Mathematical conversion
# # Task: Create a function convertSize(bytes).
# # Return KB and MB.


# # def convertSize(bytes):
# #     kb = bytes / 1024
# #     mb = bytes / (1024 * 1024)

# #     return kb, mb


# # bytes = float(input("Enter file size in bytes: "))

# # kb, mb = convertSize(bytes)

# # print("Size in KB:", kb)
# # print("Size in MB:", mb)


# # 28. Quiz Score Evaluator
# # Concept: Function with list input
# # Task: Create a function calculateScore(answers).
# # Correct answer gives +1.
# #
# # Correct answers:
# # A, B, C, D, A


# def calculateScore(answers):
#     correctAnswers = ["A", "B", "C", "D", "A"]
#     score = 0

#     for i in range(5):
#         if answers[i].upper() == correctAnswers[i]:
#             score = score + 1

#     return score


# answer1 = input("Enter answer for Question 1: ")
# answer2 = input("Enter answer for Question 2: ")
# answer3 = input("Enter answer for Question 3: ")
# answer4 = input("Enter answer for Question 4: ")
# answer5 = input("Enter answer for Question 5: ")

# answers = [answer1, answer2, answer3, answer4, answer5]

# score = calculateScore(answers)

# print("Quiz Score:", score)

# # 29. Employee Performance Rating
# # Concept: Function with multiple conditions
# # Task: Create a function performanceRating(tasksCompleted, mistakes).
# # Return:
# # Excellent
# # Good
# # Average
# # Poor
# #
# # Rules:
# # Excellent -> tasks >= 20 and mistakes <= 2
# # Good      -> tasks >= 15 and mistakes <= 5
# # Average   -> tasks >= 10 and mistakes <= 8
# # Poor      -> Otherwise


# def performanceRating(tasksCompleted, mistakes):
#     if tasksCompleted >= 20 and mistakes <= 2:
#         return "Excellent"
#     elif tasksCompleted >= 15 and mistakes <= 5:
#         return "Good"
#     elif tasksCompleted >= 10 and mistakes <= 8:
#         return "Average"
#     else:
#         return "Poor"


# tasksCompleted = int(input("Enter tasks completed: "))
# mistakes = int(input("Enter number of mistakes: "))

# rating = performanceRating(tasksCompleted, mistakes)

# print("Performance Rating:", rating)


# # 30. Smart Expense Analyzer
# # Concept: Real-time function design
# # Task: Create a function expenseAnalysis(expenses).
# # Return:
# # Total expense
# # Highest expense
# # Average expense
# # Category with highest spending


# def expenseAnalysis(expenses):
#     totalExpense = sum(expenses.values())
#     highestExpense = max(expenses.values())
#     averageExpense = totalExpense / len(expenses)

#     highestCategory = max(expenses, key=expenses.get)

#     return totalExpense, highestExpense, averageExpense, highestCategory


# expenses = {}

# n = int(input("Enter number of expense categories: "))

# for i in range(n):
#     category = input("Enter category: ")
#     amount = float(input("Enter amount: "))
#     expenses[category] = amount


# total, highest, average, category = expenseAnalysis(expenses)

# print("Total Expense:", total)
# print("Highest Expense:", highest)
# print("Average Expense:", average)
# print("Category with Highest Spending:", category)