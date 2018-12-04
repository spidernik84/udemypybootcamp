def makes_twenty(n1,n2):
    sumofnum = n1 + n2
    print(sumofnum)
    if sumofnum == 20 or ( n1 == 20 or n2 ==20):
        return True
    else:
        return False


print(makes_twenty(20, 10))
print(makes_twenty(2, 3))
print(makes_twenty(12, 8))
