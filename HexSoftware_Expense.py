import csv
import os

# File where expenses will be stored
EXPENSES_FILE = "expenses.csv"

# Categories for expenses (can be extended)
CATEGORIES = ["Food", "Transport", "Entertainment", "Bills", "Shopping", "Others"]

# Function to load existing expenses from the CSV file
def load_expenses():
    if not os.path.exists(EXPENSES_FILE):
        return []
    
    expenses = []
    with open(EXPENSES_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            expenses.append({
                "name": row[0],
                "amount": float(row[1]),
                "category": row[2],
            })
    return expenses

# Function to save expenses to the CSV file
def save_expenses(expenses):
    with open(EXPENSES_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for expense in expenses:
            writer.writerow([expense["name"], expense["amount"], expense["category"]])

# Function to add a new expense
def add_expense(expenses):
    print("\n--- Add New Expense ---")
    name = input("Enter the name of the expense: ")
    while True:
        try:
            amount = float(input("Enter the amount: $"))
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            break
        except ValueError as e:
            print(f"Invalid input. Please enter a valid number. Error: {e}")

    print("\nCategories: ", ", ".join(CATEGORIES))
    category = input("Enter the category of the expense: ").capitalize()

    while category not in CATEGORIES:
        print(f"Invalid category. Choose from: {', '.join(CATEGORIES)}")
        category = input("Enter the category of the expense: ").capitalize()

    expenses.append({"name": name, "amount": amount, "category": category})
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded.")
        return
    
    print("\n--- All Expenses ---")
    print(f"{'Name':<20} {'Amount':<10} {'Category':<15}")
    print("-" * 45)
    for expense in expenses:
        print(f"{expense['name']:<20} ${expense['amount']:<10.2f} {expense['category']:<15}")
    print("-" * 45)

# Function to show expenses summary by category
def show_summary(expenses):
    if not expenses:
        print("\nNo expenses recorded.")
        return

    summary = {}
    for expense in expenses:
        if expense["category"] not in summary:
            summary[expense["category"]] = 0
        summary[expense["category"]] += expense["amount"]

    print("\n--- Expenses Summary by Category ---")
    print(f"{'Category':<15} {'Total Amount':<10}")
    print("-" * 30)
    for category, total in summary.items():
        print(f"{category:<15} ${total:<10.2f}")
    print("-" * 30)

# Main function to interact with the user
def main():
    expenses = load_expenses()
    
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses Summary by Category")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            show_summary(expenses)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option (1-4).")

if __name__ == "__main__":
    main()
