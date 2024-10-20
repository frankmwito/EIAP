# Private attributes

class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.name = name
        self.account_number = account_number
        self.__balance = balance  # Private attribute
        
    def deposit(self):
        amount = float(input("Enter the amount to deposit: $"))
        if amount < 0:
            print("Invalid deposit amount.")
        else:
            self.__balance += amount
            print(f"Successfully deposited ${amount}.")
    
    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: $"))
        if amount > self.__balance:
            print("Insufficient balance.")
        elif amount < 0:
            print("Invalid withdrawal amount.")
        else:
            self.__balance -= amount
            print(f"Successfully withdrew ${amount}.")
    
    def check_balance(self):
        return f"Current balance: ${self.__balance}"
        

# User interaction
name = input("Enter your name: ")
account_number = input("Enter your account number: ")

bankaccount1 = BankAccount(account_number, name)

bankaccount1.deposit()
bankaccount1.withdraw()
print(bankaccount1.check_balance())
