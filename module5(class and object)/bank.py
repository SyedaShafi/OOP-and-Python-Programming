class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        print(self.balance)
    
    def deposit(self, amount):
        if(amount > 0):
            self.balance += amount

    def withdraw(self, amount):
        if( amount < self.min_withdraw):
            print(f'insufficient amout.It should be greater than {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f"Amount should be greater than {self.max_withdraw}")
        else:
            self.balance -= amount
            print(f"Withdraw successful total wothdraw: {amount} \ncurrent amount {self.get_balance()}")


brac_bank = Bank(15000000)
brac_bank.withdraw(200)

brac_bank.deposit(300)
brac_bank.get_balance()







