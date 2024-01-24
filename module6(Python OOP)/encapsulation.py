class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name #public
        self._branch = 'banani 11' #protected
        self.__initial_deposit = initial_deposit #private attribute

    def deposit(self, amount):
        self.__initial_deposit += amount

    def get_balance(self):
        return self.__initial_deposit

user1 = Bank('Mr. XYZ', 120000)
# print(user1.initial_deposit)#not accessible

print(user1.get_balance())
user1.deposit(120000)
print(user1.get_balance())
print(user1._branch)





