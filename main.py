from tracker import add_expense, total_expense, list_expenses

add_expense("Coffee", 3.5)
add_expense("Lunch", 8.0)
add_expense("Book", 15.0)

print("Expenses:")
for name, amount in list_expenses():
    print(f"- {name}: ${amount:.2f}")

print(f"\nTotal: ${total_expense():.2f}")
