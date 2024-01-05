t = input()
t = int(t)
while(t>0):
    num = input() 
    tmp = ""
    for ele in num:
       tmp += ele +' '
    print(tmp[::-1])
    t-=1