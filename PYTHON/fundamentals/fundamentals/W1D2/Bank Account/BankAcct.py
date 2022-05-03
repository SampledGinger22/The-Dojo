# class User:
    
#     bank_name = "Dojo Bank"
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.account_balance = 10

#     def make_deposit(self, amount):
#         self.account_balance += amount
#         return self

#     def make_withdrawl(self, amount):
#         self.account_balance -= amount
#         return self

#     def display_user_balance(self):
#         print("User:", self.name,", Balance:", self.account_balance)
#         return self


# Guido = User("Guido", "Guido@python.com")
# Stewie = User("Stewie", "stewie@gmail.com")
# Malcome = User("Malcome", "malcome@gmail.com")

# Guido.make_deposit(500).make_deposit(300).make_deposit(200).make_withdrawl(50).display_user_balance()
# Stewie.make_deposit(1000).make_deposit(50).make_withdrawl(1000).make_withdrawl(100).display_user_balance()