class BankAccount:

    bank_name = "Dojo Bank"
    all_accounts = []
    def __init__(self, acct_name, int_rate = 0.025, balance = 0):
        self.acct_name = acct_name
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        # return self

    def withdraw(self, amount):
        if self.balance < amount:
            self.withdraw(5)
            print("Insufficient Funds: Charging a $5 fee. New Balance:", self.balance)
        else:
            self.balance -= amount 
        # return self

    def display_account_info(self):
        print(self.acct_name,"Balance: $", round(self.balance,2))

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        # return self

class User:
    
    bank_name = "Dojo Bank"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount("Checking", 0.025, 0)


    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(self.name, self.account.balance)
        return self


Guido = User("Guido", "Guido@python.com")
Stewie = User("Stewie", "stewie@gmail.com")
Malcome = User("Malcome", "malcome@gmail.com")

Guido.make_deposit(500).make_deposit(300).make_deposit(200).make_withdrawl(50).display_user_balance()
Stewie.make_deposit(1000).make_deposit(50).make_withdrawl(1000).make_withdrawl(51).display_user_balance()
