n, q = map(int, input().split())
lst = list(map(int, input().split()))
pre_sum = [0]
tmp = 0
for num in lst:
    tmp += num
    pre_sum.append(tmp)

while q>0:
    a, b = map(int, input().split())
    print(pre_sum[b] - pre_sum[a-1])
    q-=1


