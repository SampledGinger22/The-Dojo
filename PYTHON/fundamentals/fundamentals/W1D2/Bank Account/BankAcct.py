class BankAccount:

    bank_name = "Dojo Bank"
    all_accounts = []
    def __init__(self, name, int_rate = 0.025, balance = 0):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            self.balance - 5
            print("Insufficient Funds: Charging a $5 fee. New Balance:", self.balance)
        else:
            self.balance -= amount 
        return self

    def display_account_info(self):
        print(self.name,"Balance: $", round(self.balance,2))

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

Checking = BankAccount("Checking", 0.025, 500)
Savings = BankAccount("Savings", 0.05, 1000)

Checking.deposit(500).deposit(600).deposit(700).withdraw(955).yield_interest().display_account_info()
Savings.deposit(12000).deposit(20).withdraw(2000).withdraw(5000).withdraw(9853).withdraw(50).yield_interest().display_account_info()
