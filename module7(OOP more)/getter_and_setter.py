class Mobile:
    fp = "yes"
    def __init__(self) -> None:
        self.model = 'Default Model'
        
    def class_method(cls):
        cls.fp = "no never"


    # setter method
    def set_model(self, model):
        self.model = model

    # getter method
    def get_model(self):
        print("The model name is :" +  self.model, self.fp)


obj = Mobile()
obj.class_method()
obj.get_model()
obj.set_model('Model xyz')
Mobile.fp = 'NOOOOOO'
obj.get_model()

obj2 = Mobile()
obj2.get_model()