class Calculator:
    def add(self, n1, n2):
        return n1+n2
    def sub(self, n1, n2):
        return n1-n2
    def mul(self, n1, n2):
        return n1*n2
    def div(self, n1, n2):
        return n1/n2
    
myObj = Calculator()
a,b = map(int, input().split())
print(myObj.add(a, b))
print(myObj.sub(a, b))
print(myObj.mul(a, b))
print(myObj.div(a, b))

