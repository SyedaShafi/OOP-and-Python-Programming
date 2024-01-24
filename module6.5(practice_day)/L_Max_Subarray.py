t = int(input())
while t>0:
    n = int(input())
    lst = list(map(int, input().split()))
    # print(lst)
    i = 1
    res = []
    while i<=n:
        j=0
        while j<n:
            if (len(lst)-j ) >= i: 
                tmp = max(lst[j:j+i])
                print(tmp, end=' ')
                # print(lst[j:j+i])
            j+=1
        i+=1
    print()
    t-=1

