class Phone:
    manufactured = 'China'

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_msg(self, phone, sms):
        print(f'sending this msg {sms} from the phone "{phone}"')


obj = Phone('mr.X', 'Samsung', 1300000)

obj.send_msg("samsung", "message i want to send")
print(obj.brand)



