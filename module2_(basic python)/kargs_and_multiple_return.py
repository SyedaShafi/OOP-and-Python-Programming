
def full_name(first, last):
    name = f'{first} {last}'
    return name
# take order parameter
# name = full_name('shafi' ,'begum')

# we reorder it
name = full_name(last = 'begum', first = 'shafi')
print(name)


def famous_name(first, last, **addition):
    print(addition)
    for key, value in addition.items():
        print(key, value)
    return f"{first} {last}"

name = famous_name("taher", "ali", model = "model", m1 = "for ", mm = "none")
print(name)


# returning multiple values
def a_lot(num1, num2):
    sum = num1+num2
    mul = num1*num2
    remain = num1 - num2
    return [sum, mul, remain]
    # return sum, mul, remain

values = a_lot(3, 7)
print (values)






