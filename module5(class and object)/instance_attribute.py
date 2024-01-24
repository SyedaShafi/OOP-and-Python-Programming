class Shop:
    shopping_mall = 'Jamuna'
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)
    

    
cus1 = Shop('muna')
cus2 = Shop('eka')

cus1.add_to_cart('burka')
cus1.add_to_cart('niqab')

cus2.add_to_cart('dress')
cus2.add_to_cart('chocolate')

print(cus1.cart)
print(cus2.cart)

