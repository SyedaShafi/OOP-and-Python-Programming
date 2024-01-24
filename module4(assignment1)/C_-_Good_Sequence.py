from collections import Counter
n = int(input())
lst = list(map(int, input().split()))
cnt_ele = Counter(lst)
# print(cnt_ele)
ans = 0 
for key, val in cnt_ele.items():
    if(key > val):
        ans += val
    elif(key < val):
        ans+= abs(key-val)
        

print(ans)



