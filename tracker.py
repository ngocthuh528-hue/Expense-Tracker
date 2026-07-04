expenses = []


def add_expense(name, amount):
    expenses.append((name, amount))


def total_expense():
    return sum(amount for _, amount in expenses)


def list_expenses():
    return expenses
