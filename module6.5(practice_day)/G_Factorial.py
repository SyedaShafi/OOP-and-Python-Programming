t = int(input())
while(t>0):
    n = int(input())
    sum = 1
    for i in range(2,n+1):
        sum*=i
    print(sum)
    t-=1

