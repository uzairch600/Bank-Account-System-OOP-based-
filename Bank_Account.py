# Bank Account System (OOP-based)
# Author: Uzair Muhammad


class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful! Your new balance is: {self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance! Your current balance is: {self.balance}")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrawal successful! Your new balance is: {self.balance}")
        else:
            print("Withdrawal amount must be positive!")

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: {self.balance}")


def perform_action(account):
    """Ask user for the action to perform without using a while loop."""
    
    print("\n--- Menu ---")
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Check balance")
    print("4. Exit")
    
    choice = input("Choose an option (1/2/3/4): ")
    
    if choice == '1':
        amount = float(input("Enter the amount to deposit: "))
        account.deposit(amount)
        perform_action(account)
    
    elif choice == '2':
        amount = float(input("Enter the amount to withdraw: "))
        account.withdraw(amount)
        perform_action(account)
    
    elif choice == '3':
        account.check_balance()
        perform_action(account)
    
    elif choice == '4':
        print("Thank you for using the Bank Account System!")
    
    else:
        print("Invalid choice. Please select a valid option.")
        perform_action(account)


def main():
    print("Welcome to the Bank Account System!")
    
    account_holder = input("Enter the account holder's name: ")
    account_number = input("Enter the account number: ")
    
    initial_balance = float(input("Enter initial balance (default is 0): ") or 0)
    
    account = BankAccount(account_holder, account_number, initial_balance)
    
    perform_action(account)


if __name__ == "__main__":
    main()
