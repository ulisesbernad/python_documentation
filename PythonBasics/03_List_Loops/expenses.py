expenses = [10.50, 8, 5, 15, 20, 5, 3]
n=0
for expense in expenses:
    n= n+ expense
print('You spent $',n, " on lunch this week.",sep='')

#Another way to do the same:
total= sum(expenses)

print("You spent $",total, " on lunch this week.",sep='')