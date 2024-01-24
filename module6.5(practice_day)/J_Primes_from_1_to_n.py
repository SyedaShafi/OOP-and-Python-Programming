n = int(input())
N = 10**3+7
is_prime = [True] * N

p = 2

while(p*p <= N):
    if(is_prime[p] == True):
        for i in range(p*p, N, p):
            is_prime[i] = False
    p+=1

for i in range (2, n+1):
    if(is_prime[i]):
        print(i, end=' ')
        
