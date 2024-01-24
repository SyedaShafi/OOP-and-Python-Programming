class Shop:
    cart = []
    def __init__(self, buyer):
        self.buyer = buyer
    
    def add_to_cart(self, item):
        self.cart.append(item)


customer = Shop('Saki')
customer.add_to_cart('cake')
customer.add_to_cart('chocolate')
customer.add_to_cart('phone')

cus2 = Shop('nadira')
cus2.add_to_cart('alu')
cus2.add_to_cart('tomato')
print(customer.cart)
print(cus2.cart)




