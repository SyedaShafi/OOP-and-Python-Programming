# **kwargs:
# It is used to pass arguments to a function in a way that is similar to key, value pairs.

# def test(**a):
#     for key, val in a.items():
#         print(key, val)

# test( name= "Mr. X", age= 23, lst= [1, 2,3])



# *args:
# It is used when the number of arguments passing to a function is unknown.


def test(*a):
    for ele in a:
        print(ele)


test("name", 23, 55, [1, 2,3])
