numbers = [23, 6, 78, 90, 45, 37, 8,245]
odds = []
for num in numbers:
    if num%2 == 1:
        odds.append(num)
print(odds)


# comprehensive method
odd_nums = [num for num in numbers if num%2 ==1]
print(odd_nums)


numbers =[7,8,5,4,3,2,4]
print(numbers[::-1])