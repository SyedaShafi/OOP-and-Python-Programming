k, s = map(int, input().split())
i = 0
cnt = 0
j = 0
while(i<=k):
    j=0
    while(j<=k):
        m = s - (i + j)
        if (m>=0 and m<=k):
            # print(i, j, m)
            cnt+=1
        j+=1
    i+=1

print(cnt)


