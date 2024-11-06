import sqlite3
import datetime

# Create a connection to the database
def DatabaseCreat():        
    conn = sqlite3.connect('expense_tracker.db')

    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS expenses 
    (id INTEGER PRIMARY KEY,
    date TEXT,
    category TEXT,
    description TEXT,
    amount REAL)''')

    conn.commit()
    conn.close()
    

def DataConnection():
    conn = sqlite3.connect('expense_tracker.db')
    cur = conn.cursor()

    while True:
        print("Select an option: ")
        input_option = input("1. Add Expense\n2. View Expenses\n3. Exit\n")

        if input_option == '1':
            date = datetime.datetime.now().strftime('%Y-%m-%d')
            description = input("Enter the description: ")

            cur.execute("SELECT DISTINCT category FROM expenses")

            categories = cur.fetchall()

            print("Select a category by number: ")

            for i, category in enumerate(categories):
                print(f"{i+1}. {category[0]}")

            print(f"{len(categories)+1}. Create new category")
            
            category_option = input()

            if category_option == str(len(categories)+1):
                category = input("Enter the category: ")
            else:
                category = categories[int(category_option)-1][0]


            amount = float(input("Enter the amount: "))

            cur.execute("INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)", (date, category, description, amount))
            conn.commit()

        elif input_option == '2':
           
            choice_option = input("1. View all expenses\n2. View monthly expenses by category\n3. View yearly expenses\n")
            if choice_option == "1":
                cur.execute("SELECT * FROM expenses")
                expenses = cur.fetchall()
                for expense in expenses:
                    print(expense)
            elif choice_option == "2":
                month = input("Enter the month (MM): ")

                cur.execute("SELECT category, SUM(amount) FROM expenses WHERE strftime('%m', date) = ?  GROUP BY category", (month,))

                expense = cur.fetchall()
                for expense in expense:
                    print(f"Category : {expense[0]}, Total Amount : {expense[1]}")

            elif choice_option == "3":
                year = input("Enter the year (YYYY): ")

                cur.execute("SELECT category, SUM(amount) FROM expenses WHERE strftime('%Y', date) = ? GROUP BY category", (year,))

                expense = cur.fetchall()
                for expense in expense:
                    print(f"Category : {expense[0]}, Total Amount : {expense[1]}")

        elif input_option == '3':  
            break
        else:
            print("Invalid input. Please try again.")

        repeat = input("Do you want to continue? (Y/N) ")
        
        if repeat.lower() != 'y':
            break
    conn.close()

DatabaseCreat()
DataConnection()




