t = int(input())
while t>0:
    n = int(input())
    lst = list(map(int, input().split()))
    i = 1
    cnt = 0
    while i<=n:
        j = 0
        while j<n:
            if(len(lst) - j >= i):
                tmp = lst[j : j+i]
                # print(tmp)
                tmp1 = tmp.copy()
                tmp1 = sorted(tmp1)
                if(tmp1 == tmp):
                    cnt+=1
            j+=1
        i+=1
    print(cnt)
    t-=1