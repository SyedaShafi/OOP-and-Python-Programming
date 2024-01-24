n = int(input())
lst = list(map(int, input().split()))
def is_divisible(arr):
    for ele in arr:
        if(ele%2):
            return False
    return True
cnt=0
while(is_divisible(lst)):
    for e in range(len(lst)):
        lst[e] = int(lst[e]/2)
    cnt+=1
print(cnt)
