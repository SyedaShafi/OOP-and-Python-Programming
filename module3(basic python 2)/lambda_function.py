# def double(x):
#     return x*2
# print(double(3))

double = lambda num: num*2
sqr = lambda num: num*num
print(double(9))
print(sqr(5))

add = lambda x, y: x+y
print(add(3, 7))


nums = [1, 23, 4, 5, 6, 7, 77, 79]

# double_nums = map(double, nums)
double_nums = map(lambda num: num*2, nums)
print(list(double_nums))

actors = [ 
    {'name': 'sabana', 'age': 55},
    {'name': 'x', 'age': 23},
    {'name': 'y', 'age': 33},
    {'name': 'z', 'age': 54},
    {'name': 'kk', 'age': 13}]


juniors = filter(lambda actor: actor['age']<40, actors)
print(list(juniors))

