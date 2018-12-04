# takes an array and sums all numbers except the ones between
# 6 and 9

def summer69(arr):
    total = 0
    add = True
    for number in arr:
        while add:
            if number != 6:
                total += number
                print(number)
                break
            else:
                add = False
        while not add:
            if number != 9:
                break
            else:
                add = True
                break
    return total


print(summer69([1,3,5,6,2,3,4,9,11]))





# 1, 7, 8, 2, 6, 4, 9, 8