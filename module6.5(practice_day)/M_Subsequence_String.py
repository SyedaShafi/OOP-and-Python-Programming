str1 = input()
idx = 0
cnt = 0
for ele in str1:
    if ele == 'l':
        cnt += 1
    if(ele == list[idx] and cnt < 3):
        idx+=1
if(idx == 5):
    print('YES')
else:
    print('NO')