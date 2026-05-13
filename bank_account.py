class Account:
    def _init_(self, name, balance=0):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"You deposited {amount} successfully. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.__balance}")
        else:
            print("Insufficient balance.")


class Savings(Account):
    def __init__(self, name, balance=0):
        super()._init_(name, balance)
        self.interest_rate = 0.02
        self.withdraw_limit = 100

    def withdraw(self, amount):

        if amount > self.withdraw_limit:

            print(f"Withdrawal denied. Limit is ${self.withdraw_limit}")

        else:

            super().withdraw(amount)
    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest applied. New balance: {self.get_balance()}")




#Test the Savings account
print("---Savings Account---")

savings = Savings("Alice", 1000)

print(f"Initial balance: {savings.get_balance()}")

savings.deposit(500)

savings.withdraw(200)

savings.apply_interest()
