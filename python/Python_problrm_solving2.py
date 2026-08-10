# 1. Find the First Peak
# Task: A sequence contains daily website visitors. Find the first day whose visitor count is greater than both the previous and next day. Do not check the first and last elements.
# Example Input:
# visitors = [120, 150, 140, 180, 200, 170, 160]
# Example Output: First peak: 150

# visitors = [56, 343, 78, 3947, 45]
# peaks = [curr for prev, curr, nxt in zip(visitors, visitors[1:], visitors[2:])
#          if curr > prev and curr > nxt]

# if peaks:
#     print("First peak:", peaks[0])
#     print("Highest peak:", max(peaks))
# else:
#     print("No peak found")


# 2. Running Balance Monitor
# Task: You have a starting bank balance. Each number is a transaction.
# Positive means deposit and negative means withdrawal.
# After every transaction, print 'Overdrawn' if balance is negative,
# 'Empty' if it is zero, otherwise print the balance.
# Example Input: balance = 1000 transactions = [500, -300, -1200, 800]
# Example Output: 1500 1200 Overdrawn 400

balance = int(input("Enter starting balance: "))

transactions = list(map(int, input("Enter transactions separated by space: ").split()))
for transaction in transactions:
    balance += transaction
    if balance < 0:
        print("Overdrawn")
    elif balance == 0:
        print("Empty")
    else:
        print(balance)