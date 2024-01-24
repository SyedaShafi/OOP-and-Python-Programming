class Father:
    def __init__(self, v) -> None:
        self.v = v
        print("Father constructor is called.", v)

class Son(Father):
    def __init__(self, v) -> None:
       super().__init__(v)
       self.vv = v+1000
       print("Child constructor is called.", self.vv)
    def show(self):
        print("This is the show method.")

s = Son(1000)













