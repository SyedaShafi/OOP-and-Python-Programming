class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []
    
    def add_to_cart(self, item, price, quantity):
        product = {'item' : item, 'price' : price, 'quantity': quantity}
        self.cart.append(product)

    def checkout(self):
        total = 0
        for item in self.cart:
            total += int(item['price'])*int(item['quantity'])
        # print(total)
        print(f'you need to pay {total}')

    def remove_from_cart(self, item_name):
        for item in self.cart:
            if item['item']==item_name:
                self.cart.remove(item)
            

user1 = Shopping('rocky')
user1.add_to_cart('alu', 50, 4)
user1.add_to_cart('dim', 11, 10)
user1.add_to_cart('rice', 55, 6)

user1.checkout()
print(user1.cart)
print("\n\n")
user1.remove_from_cart('alu')
print(user1.cart)





