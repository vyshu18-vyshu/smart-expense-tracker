import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


# Create file if not exists
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Date", "Category", "Amount", "Description"])


# Add expense
def add_expense():
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME, mode='r') as file:
        reader = list(csv.reader(file))
        expense_id = len(reader)

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([expense_id, date, category, amount, description])

    print("✅ Expense added successfully!\n")


# View expenses
def view_expenses():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        print("\n---- All Expenses ----")
        for row in reader:
            print(f"ID: {row[0]} | Date: {row[1]} | Category: {row[2]} | Amount: ₹{row[3]} | Desc: {row[4]}")
    print()


# Delete expense
def delete_expense():
    expense_id = input("Enter Expense ID to delete: ")
    rows = []

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    header = rows[0]
    data = rows[1:]

    updated_data = [row for row in data if row[0] != expense_id]

    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(updated_data)

    print("🗑 Expense deleted successfully!\n")


# Show total
def show_total():
    total = 0
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += float(row[3])

    print(f"\n💰 Total Expenses: ₹{total}\n")


# Main menu
def main():
    initialize_file()

    while True:
        print("====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Total")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            show_total()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()