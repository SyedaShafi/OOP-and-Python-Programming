class Mobile:
    fp = "yes"
    @classmethod
    def show_model(cls, r):
        cls.ram = r
        print(cls.ram, cls.fp)
    def show(self):
        print("Memory ", self.ram)

realme = Mobile()
Mobile.show_model(1200)

rr = Mobile()
rr.show()
