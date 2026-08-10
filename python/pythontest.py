# #  Problem 1: Student Initials

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# print(f"Student Initials: {first_name[0]}{last_name[0]}")


# # Problem 2: Login Eligibility

# age = int(input("Enter your age: "))
# if age < 13:
#     print("Child Account")
# elif 13 <= age <= 17:
#     print("Teen Account")
# else:
#     print("Adult Account")

# # Problem 3: Check First and Last Character
# check_string = input("Enter a string: ")
# first_char = check_string[0]
# last_char = check_string[-1]
# if first_char == last_char:
#     print("Same")
# else:
#     print("Different")


# #  Problem 4: Count Uppercase Letters
# count = 0
# s = input("Enter a string: ")
# for char in s:
#     if char.isupper():
#         count += 1
# print(f"Uppercase Letters: {count}")

# # Problem 5: Shopping Discount
# bill = float(input("Enter the bill amount: "))
# if bill >= 5000:
#     discount = 0.20
# elif bill >= 3000:
#     discount = 0.10
# else:
#     discount = 0
# discount_amount = bill * discount
# payable_amount = bill - discount_amount
# print(f"Discount: {discount * 100}%")
# print(f"Payable Amount: {payable_amount}")


# # Problem 6: Count Digits 
# count = 0
# s = input("Enter a string: ")
# for char in s:
#     if char.isdigit():
#         count += 1
#     else:
#         continue
# print(f"Digits: {count}")


# # Problem 7: Membership Validation 
# validate_membership = int(input("Enter your age: "))
# if validate_membership >= 18:
#     membership_type = input("Enter membership type (Gold/Silver): ")
#     if membership_type.lower() == "gold":
#         print("Premium Access")
#     elif membership_type.lower() == "silver":
#         print("Standard Access")
#     else:
#         print("Invalid Membership Type")
# else:
#     print("Access Denied")


# # Problem 8: Print Odd Index Characters

# odd=""
# s = input("Enter a string: ")
# for i in range(len(s)):
#     if i % 2 == 1:
#         odd += s[i]
#     elif i % 2 == 0:
#         continue
#     else:
#         break

# print(f"Odd index characters: {odd}")


# #  Problem 9: Password Length Checker 

# check_password = input("Enter your password: ")
# if len(check_password) < 8:
#     print("Weak Password")
# elif 8 <= len(check_password) <= 11:
#         print("Medium Password")
# else:
#         print("Strong Password")



#  Problem 10: Vowel Counter

count_vowels = 0
vowels = "aeiouAEIOU"
input_string = input("Enter a string: ")
print(f"Input String: {input_string}")
for char in input_string:
    if char in vowels:
        count_vowels += 1
    else:
        continue
print(f"Vowels: {count_vowels}")