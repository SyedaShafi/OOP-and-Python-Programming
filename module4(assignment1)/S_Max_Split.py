str = input()
lst = []
cnt = 0
l = 0
r = 0
tmp = ""
for ele in str:
    if(ele == 'L'):
        l+=1
        tmp+=ele
    else:
        r+=1
        tmp+=ele
    if(l == r):
        cnt+=1
        lst.append(tmp)
        tmp = ""
        l = 0
        r = 0


print(cnt)
for ele in lst:
    print(ele)

