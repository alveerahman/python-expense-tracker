# ---------------------------------------------------------
# Project: Smart Expense Tracker
# Author: Alvee Rahman (Final Year CS Student)
# Features: File Handling, Data Management, Expense Tracking
# ---------------------------------------------------------

import os

FILE_NAME = "expenses.txt"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            f.write("Category,Amount\n")

def add_expense():
    category = input("Enter Category (e.g. Food, Rent, Bills): ")
    amount = input("Enter Amount: ")
    
    with open(FILE_NAME, "a") as f:
        f.write(f"{category},{amount}\n")
    print(f"✔️ Added {amount} to {category}!")

def view_expenses():
    print("\n--- All Expenses ---")
    total = 0
    try:
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()[1:] # Skip header
            if not lines:
                print("No expenses recorded yet.")
                return
            for line in lines:
                cat, amt = line.strip().split(",")
                print(f"📍 {cat}: ${amt}")
                total += float(amt)
        print("-" * 20)
        print(f"💰 Total Spent: ${total}")
    except FileNotFoundError:
        print("No data file found.")

def main():
    initialize_file()
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Goodbye! Stay on budget.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()