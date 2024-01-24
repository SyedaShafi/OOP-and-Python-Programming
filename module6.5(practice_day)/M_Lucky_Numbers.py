a, b = map(int, input().split())
ans = []
for i in range(a,b+1):
    tmp = str(i)
    tmp = list(tmp)
    f = False
    for ele in tmp:
        if(ele == '4' or ele == '7'):
            f = True
        else:
            f = False
            break
    if(f):
       ans.append(i)

if(len(ans) > 0):
    for ele in ans:
        print(ele, end = ' ')
else :
    print(-1)



