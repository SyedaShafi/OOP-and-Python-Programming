n = int(input())
while n>0:
    s, t = map(str, input().split())
    s_len = len(s)
    t_len = len(t)
    i = 0
    tmp = ""
    while i < max(s_len, t_len):
        if(i<s_len):
            tmp+=s[i]
        if(i<t_len):
            tmp+=t[i]
        i+=1
    print(tmp)
    n-=1



