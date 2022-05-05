class User:
    
    bank_name = "Dojo Bank"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 10

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print("User:", self.name,", Balance:", self.account_balance)


Guido = User("Guido", "Guido@python.com")



Guido.make_withdrawl(20).display_user_balance()

