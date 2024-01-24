n = int(input())
nums = input()
lst = list(map(int, nums.split()))
mx = max(lst)
mn = min(lst)
idx_mx = lst.index(mx)
idx_mn = lst.index(mn)
lst[idx_mx], lst[idx_mn] = lst[idx_mn], lst[idx_mx]

for ele in lst:
    print(ele, end=" ")