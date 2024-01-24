def call():
    print("call function")
    return 'call done'

class Phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'
    features = ['camera', 'speakers', 'hammer']
    def call(self):
        self.item = 'this is the item'
        print(f'call from class function {self.price}')

    def send_msg(self, name, msg):
        print(f'sending msg to MR. {name} : {msg}')
        print(self.item)
        print(self.price)


myPhone = Phone()
print(myPhone.features)
myPhone.call()
myPhone.send_msg('user', 'this is the message')


