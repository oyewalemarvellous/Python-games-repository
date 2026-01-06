class Account:
    def __init__(self,amount):
        self.amount  = amount
    def check_balance(self):
        print(self.amount, "is your amount")
    def withdraw(self, price):
        self.amount -= price
    def deposit(self,number):
        self.amount += number 
p1 = Account(3000)
p1.check_balance()
p1.withdraw(500)
p1.check_balance()
p1.deposit(4000)
p1.check_balance()

