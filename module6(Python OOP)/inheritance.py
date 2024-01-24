# common things in one place
# base class
class Gadget:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin
        
    def run(self):
        return f'running laptop: {self.brand}'

class Laptop:
    def __init__(self, memory, SSD) -> None:
        self.memory = memory
        self.SSD = SSD
    
    def coding(self):
        return f'learning pyhton'

class Phone(Gadget):
    def __init__(self,brand, price, color, origin, dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)

    def phone_call(self, number, text):
        return f'Sending SMS to : {number} with: {text}'
    
    def __repr__(self) -> str:
        return f'Phone has Dual sim = {self.dual_sim}'

class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel
    def change_lens(self):
        pass


myPhone = Phone('iphone', 120000, 'silver', 'china', True)
print(myPhone.brand)
print(myPhone)



