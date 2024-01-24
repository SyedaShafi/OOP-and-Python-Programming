class Mobile:
    var = 'yes'
    def show(self):
        print('this is the show function')
RealMe = Mobile()
redmi = Mobile()
geek = Mobile()
print('RealMe: ', RealMe.var)
print('Redmi: ', redmi.var)
print('Geek: ', geek.var)
print()
Mobile.var = 'modified using class name'
print('RealMe: ', RealMe.var)
print('Redmi: ', redmi.var)
print('Geek: ', geek.var)
print()
redmi.var = 'modified using object name'
print('RealMe: ', RealMe.var)
print('Redmi: ', redmi.var)
print('Geek: ', geek.var)
print()
