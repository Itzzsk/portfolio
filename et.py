import json
import os

class Expense:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

    def to_dict(self):
        return {
            'description': self.description,
            'amount': self.amount
        }

    @staticmethod
    def from_dict(data):
        return Expense(data['description'], data['amount'])

    def __str__(self):
        return f"{self.description}: ${self.amount:.2f}"


class ExpenseTracker:
    def __init__(self, filename='expenses.json'):
        self.expenses = []
        self.filename = filename
        self.load_expenses()

    def add_expense(self, description, amount):
        expense = Expense(description, amount)
        self.expenses.append(expense)
        self.save_expenses()
        print(f"Added expense: {expense}")

    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("Expenses:")
            for index, expense in enumerate(self.expenses, start=1):
                print(f"{index}. {expense}")

    def edit_expense(self, index, description, amount):
        if 0 <= index < len(self.expenses):
            self.expenses[index].description = description
            self.expenses[index].amount = amount
            self.save_expenses()
            print(f"Updated expense: {self.expenses[index]}")
        else:
            print("Invalid index.")

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            removed_expense = self.expenses.pop(index)
            self.save_expenses()
            print(f"Deleted expense: {removed_expense}")
        else:
            print("Invalid index.")

    def save_expenses(self):
        with open(self.filename, 'w') as file:
            json.dump([expense.to_dict() for expense in self.expenses], file)

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.expenses = [Expense.from_dict(item) for item in data]

    def run(self):
        while True:
            print("\nExpense Tracker")
            print("1. Add Expense")
            print("2. View Total Expenses")
            print("3. View All Expenses")
            print("4. Edit Expense")
            print("5. Delete Expense")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                description = input("Enter expense description: ")
                amount = float(input("Enter expense amount: "))
                self.add_expense(description, amount)
            elif choice == '2':
                total = self.total_expenses()
                print(f"Total Expenses: ${total:.2f}")
            elif choice == '3':
                self.view_expenses()
            elif choice == '4':
                self.view_expenses()
                index = int(input("Enter the index of the expense to edit: ")) - 1
                description = input("Enter new expense description: ")
                amount = float(input("Enter new expense amount: "))
                self.edit_expense(index, description, amount)
            elif choice == '5':
                self.view_expenses()
                index = int(input("Enter the index of the expense to delete: ")) - 1
                self.delete_expense(index)
            elif choice == '6':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()