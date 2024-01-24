class Shop:
    # products = []
    def __init__(self) -> None:
        self.products = []

    def add_product(self, product_name):
        # product_name = 'rice'
        self.products.append(product_name)

    def buy_product(self, name):
        # self.name = name
        if name in self.products:
            print (f'Congress product {name} is available ')
        else:
            print(f'Product {name} not available')

class Product(Shop):
    def __init__(self) -> None:
        super().__init__()

p1 = Product()
p1.add_product('alu')
print(p1.products)
p1.buy_product('rice')




