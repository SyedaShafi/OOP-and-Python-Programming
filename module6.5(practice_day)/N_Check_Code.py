a, b = map(int, input().split())
s = input()
cnt = s.count('-')
if(cnt == 1):
    if(s[a] == '-'):
        print('Yes')
    else:
        print('No')
else:
    print('No')

