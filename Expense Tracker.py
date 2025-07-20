import json
import os

DATA_FILE = "expenses.json"

class Expense:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def to_dict(self):
        return {
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
            "description": self.description
        }

class ExpenseTracker:
    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if not os.path.exists(self.data_file):
            return []
        with open(self.data_file, "r") as file:
            expenses_list = json.load(file)
            return [Expense(**exp) for exp in expenses_list]

    def save_expenses(self):
        with open(self.data_file, "w") as file:
            json.dump([exp.to_dict() for exp in self.expenses], file, indent=4)

    def add_expense(self, date, category, amount, description):
        new_expense = Expense(date, category, amount, description)
        self.expenses.append(new_expense)
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        print("\n--- Expense List ---")
        for i, exp in enumerate(self.expenses, 1):
            print(f"{i}. {exp.date} | {exp.category} | ₹{exp.amount} | {exp.description}")
        print("---------------------\n")

    def total_expense(self):
        total = sum(exp.amount for exp in self.expenses)
        print(f"Total expenses: ₹{total}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (Food, Travel, etc.): ")
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
            description = input("Enter description: ")
            tracker.add_expense(date, category, amount, description)
            tracker.save_expenses()
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.total_expense()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

