str = input()
str = list(str.split())
it = len(str)
i = 0
for item in str:
    i+=1
    if(i == it):
        print(item[::-1], end="")
    else:
        print(item[::-1], end=" ")

