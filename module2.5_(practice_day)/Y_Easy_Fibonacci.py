n = int(input())
a = 0
b = 1
if(n==1): 
    n-=1
    fibo = [0]
else:
    n = n-2
    fibo = [0, 1]
while n > 0:
    fibo.append(a+b)
    a = fibo[len(fibo)-1]
    b = fibo[len(fibo)-2]
    n-=1

# print(*fibo, sep = ' ')
for i in fibo:
    print(i, end=" ")
    i+=1