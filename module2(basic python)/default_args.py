def sum(num1, num2, *num3):
    result = num1+num2
    for num in num3:
        result+=num
    return result
total  = sum(90, 10, 6, 6,7 )
print(total)




def do_a_lot(*args):
    print(args)





do_a_lot(2, 3,4 ,5,6,7,7,78)