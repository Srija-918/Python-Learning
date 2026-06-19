expenses=[]
for i in range(5):
    items=int(input("Enter 5 expenses: "))
    expenses.append(items)
print(expenses)
print("Total expenses ",sum(expenses))