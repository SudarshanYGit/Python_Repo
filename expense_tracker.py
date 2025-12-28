from datetime import date

FILENAME = "expenses.txt"

def create_file():
    try:
        open(FILENAME, "x")
    except FileExistsError:
        pass

def add_expense():
    try:
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category (Food/Travel/Shopping/etc): ")
        today = date.today()

        with open(FILENAME, "a") as file:
            file.write(f"{today},{amount},{category}\n")

        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount!")

def view_expenses():
    try:
        with open(FILENAME, "r") as file:
            print("\nDate         Amount   Category")
            print("-" * 30)
            for line in file:
                d, a, c = line.strip().split(",")
                print(f"{d}   ₹{a}   {c}")
    except FileNotFoundError:
        print("No expenses found.")

def total_expenses():
    total = 0
    with open(FILENAME, "r") as file:
        for line in file:
            _, amount, _ = line.strip().split(",")
            total += float(amount)

    print(f"\n Total Expenses: ₹{total}")

def category_summary():
    summary = {}

    with open(FILENAME, "r") as file:
        for line in file:
            _, amount, category = line.strip().split(",")

            if category in summary:
                summary[category] += float(amount)
            else:
                summary[category] = float(amount)

    print("\n Category-wise Expenses:")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt}")

def menu():
    create_file()

    while True:
        print("\n====== EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category-wise Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice!")

menu()
