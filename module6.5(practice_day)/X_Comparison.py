s = input()
tmp = s
for i in range(1, len(s)):
    tmp1 = s[0:i]
    tmp2 = s[i:len(s)]
    tmp1 = ''.join(sorted(tmp1))
    tmp2 = ''.join(sorted(tmp2))
    # print(tmp1)
    # print(tmp2)
    tmp2 = tmp1 + tmp2
    tmp = min(tmp, tmp2)
    # print('tmp :' , tmp)

print(tmp)