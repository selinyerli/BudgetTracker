import json

# Function to add an expense
def add_expense(expenses, description, amount):
    expenses.append({"description": description, "amount": amount})
    print(f"Added expense: {description}, Amount: {amount}")


# Function to calculate total expenses
def get_total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


# Function to calculate remaining balance
def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)


# Function to display budget details
def show_budget_details(budget, expenses):
    print(f"Total Budget: {budget}")
    print("Expenses:")
    for expense in expenses:
        print(f"- {expense['description']}: {expense['amount']}")
    print(f"Total Spent: {get_total_expenses(expenses)}")
    print(f"Remaining Budget: {get_balance(budget, expenses)}")


# Function to load budget data from a file
def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data["initial_budget"], data["expenses"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []


# Function to save budget data to a file
def save_budget_details(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


# Main function
def main():
    print("Welcome to the Budget App")
    filepath = 'budget_data.json'

    # Load budget and expenses
    initial_budget, expenses = load_budget_data(filepath)

    # Ask for the initial budget if not set
    if initial_budget == 0:
        while True:
            try:
                initial_budget = float(input("Please enter your initial budget: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    budget = initial_budget

    # Main loop
    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            description = input("Enter expense description: ")
            while True:
                try:
                    amount = float(input("Enter expense amount: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            add_expense(expenses, description, amount)

        elif choice == "2":
            show_budget_details(budget, expenses)

        elif choice == "3":
            save_budget_details(filepath, initial_budget, expenses)
            print("Exiting Budget App. Goodbye!")
            break

        else:
            print("Invalid choice, please choose again!")


# Run the script
if __name__ == "__main__":
    main()
