x, n= map(int, input().split())
s = 0
while(n>0):
    if(n%2==0) :
        s += (x**n)
    n-=1
print(s)

