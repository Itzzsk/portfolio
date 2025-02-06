class Expense:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount
    def __str__(self):
        return f"{self.description}:  ₹{self.amount:.2f}"
class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    def add_expense(self, description, amount):
        expense = Expense(description, amount)
        self.expenses.append(expense)
        print(f"Added expense: {expense}")
    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)
    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("Expenses:")
            for expense in self.expenses:
                print(expense)
    def run(self):
        while True:
            print("\nusername : e/itzzsk")
            print("\nExpense Tracker for skanda")
            print("1. Add Expense")
            print("2. View Total Expenses")
            print("3. View All Expenses")
            print("4. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                description = input("Enter expense description: ")
                amount = float(input("Enter expense amount: "))
                self.add_expense(description, amount)
            elif choice == '2':
                total = self.total_expenses()
                print(f"Total Expenses:  ₹{total:.2f}")
            elif choice == '3':
                self.view_expenses()
            elif choice == '4':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()