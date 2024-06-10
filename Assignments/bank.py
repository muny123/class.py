# Here is a basic implementation of a Banking System in Python that runs on the Command Line Interface (CLI):

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def transfer(self, amount, recipient_account):
        if self.balance >= amount:
            self.balance -= amount
            recipient_account.balance += amount
        else:
            print("Insufficient funds")

    def view_details(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")


class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance):
        self.accounts[account_number] = BankAccount(account_number, initial_balance)

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
        else:
            print("Account not found")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)
        else:
            print("Account not found")

    def transfer(self, sender_account, amount, recipient_account):
        if sender_account in self.accounts and recipient_account in self.accounts:
            self.accounts[sender_account].transfer(amount, self.accounts[recipient_account])
        else:
            print("Account not found")

    def view_account_details(self, account_number):
        if account_number in self.accounts:
            self.accounts[account_number].view_details()
        else:
            print("Account not found")


def main():
    banking_system = BankingSystem()
    while True:
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Account Details")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            account_number = input("Enter account number: ")
            initial_balance = float(input("Enter initial balance: "))
            banking_system.create_account(account_number, initial_balance)
        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            banking_system.deposit(account_number, amount)
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            banking_system.withdraw(account_number, amount)
        elif choice == "4":
            sender_account = input("Enter sender account number: ")
            receiver_account = input("Enter receiver account number: ")
            amount = float(input("Enter amount to transfer: "))
            banking_system.transfer(sender_account, receiver_account, amount)
        elif choice == "5":
            account_number = input("Enter account number: ")
            banking_system.view_account_details(account_number)
        elif choice == "6":
            break
        else:
            print("Invalid option")

