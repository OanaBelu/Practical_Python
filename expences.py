# Let's create a list of expenses
# 1. We put in a list all the amount of money we spent

# expenses = [10.50, 8, 5, 15, 20, 5, 3]
# sum = 0
#
# for x in expenses1:
#     sum = sum + x
#
# print("You spent $", sum, " on lunch this week.", sep='')

# 2. Or we can do this

# expenses = [10.50, 8, 5, 15, 20, 5, 3]
# total = sum(expenses)
#
# print("You spent $", total, " on lunch this week.", sep='')

# or we can add the expenses as an input if we know how many expenses we had ( 7 in our case )
# total = 0
# expenses = []
# for i in range(7):
#     expenses.append(float(input("Enter an expense : ")))
#
# total = sum(expenses)
# print("You spent $", total, " on lunch this week.", sep='')

# 3. Or we can add the expenses as an input also the number of expenses we had
total = 0
expenses = []
num_expenses = int(input("Enter  # of expenses: "))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense : ")))

total = sum(expenses)
print("You spent $", total, " on lunch this week.", sep='')