n = int(input())
lst = [0, 1]
a = 0
b = 1
for i in range(50):
    lst.append(a+b)
    a = b
    b = lst[len(lst)-1]

print(lst[n-1])


