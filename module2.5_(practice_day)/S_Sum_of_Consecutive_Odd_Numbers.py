t = input()
t = int(t)
while t>0:
    s = 0
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    # print(a, b)
    i = a+1
    while(i < b):
        if(i%2!=0):
            s += i
        i += 1

    print(s)
    t-=1