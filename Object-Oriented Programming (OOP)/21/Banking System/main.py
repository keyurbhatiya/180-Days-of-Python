'''
1. Banking System
Create a simple banking system with the following classes:

Classes & Attributes BankAccount

account_number (Unique ID)
account_holder (Name of the account holder)
balance (Initial balance, default is 0)

Methods:

deposit(amount) – Adds money to the account
withdraw(amount) – Deducts money from the account if sufficient balance
get_balance() – Returns the current balance
SavingsAccount (Inherits BankAccount)

interest_rate (fixed rate, e.g., 5%)

Additional method:

apply_interest() – Adds interest to the balance
Bank

Stores multiple accounts in a dictionary {account_number: BankAccount}

Methods:

add_account(account) – Adds a new account
find_account(account_number) – Returns an account if it exists
transfer(sender_acc, receiver_acc, amount) – Transfers money between accounts

'''
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: ₹{interest}. New balance: ₹{self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account
        print(f"Account {account.account_number} created for {account.account_holder}.")

    def find_account(self, account_number):
        return self.accounts.get(account_number, None)

    def transfer(self, sender_acc, receiver_acc, amount):
        sender = self.find_account(sender_acc)
        receiver = self.find_account(receiver_acc)

        if sender and receiver:
            if sender.balance >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print(f"Transferred ₹{amount} from {sender_acc} to {receiver_acc}.")
            else:
                print("Insufficient balance for transfer.")
        else:
            print("One or both accounts not found.")


# Example Usage with User Input
bank = Bank()
try:
    # Create accounts with user input
    acc_num1 = int(input("Enter account number for Account 1: "))
    acc_holder1 = input("Enter account holder name for Account 1: ")
    initial_balance1 = float(input("Enter initial balance for Account 1: "))
    acc1 = BankAccount(acc_num1, acc_holder1, initial_balance1)

    acc_num2 = int(input("Enter account number for Account 2: "))
    acc_holder2 = input("Enter account holder name for Account 2: ")
    initial_balance2 = float(input("Enter initial balance for Account 2: "))
    acc2 = SavingsAccount(acc_num2, acc_holder2, initial_balance2)

    bank.add_account(acc1)
    bank.add_account(acc2)

    # Interact with accounts
    acc1.deposit(float(input("Enter deposit amount for Account 1: ")))
    acc1.withdraw(float(input("Enter withdrawal amount for Account 1: ")))
    print(f"Balance for {acc_holder1}: ₹{acc1.get_balance()}")

    acc2.apply_interest()
    print(f"Balance for {acc_holder2} after applying interest: ₹{acc2.get_balance()}")

    transfer_amount = float(input("Enter amount to transfer from Account 1 to Account 2: "))
    bank.transfer(acc_num1, acc_num2, transfer_amount)

except ValueError:
    print("Invalid input. Please enter valid values.")

except Exception as e:
    print(f"An error occurred: {e}")

except KeyboardInterrupt:
    print("\nProgram terminated by user.")