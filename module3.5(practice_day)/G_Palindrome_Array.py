n = int(input())
str = input()
ar = list(map(int, str.split()))

ar2 = ar.copy()
ar.reverse()
if(ar2 == ar):
    print("YES")
else:
    print("NO")