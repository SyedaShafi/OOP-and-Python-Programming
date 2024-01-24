class Mobile:
    def __init__(self, data) -> None:
        self.data = data

    def show_model(self, age):
        self.age = age + 7
        print(age)

    def p(self):
        print(self.age , self.data)
        
    
obj = Mobile(100)
obj.show_model(3000)
obj.p()
