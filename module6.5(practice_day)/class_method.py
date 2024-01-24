class A:
    var = 999
    def show(self):
        print("This is the show function")
    @classmethod
    def is_var(cls):
        cls.var = 10000

obj = A()
obj.var = 122
# A.is_var()
# A.show()

print(A.var)
print(obj.var)