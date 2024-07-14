class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")

# For testing purposes
if __name__ == "__main__":
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(20)
    account.display_balance()
