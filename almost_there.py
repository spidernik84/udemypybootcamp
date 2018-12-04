def almostthere(number):
    near_100 = abs(100 - number)
    near_200 = abs(200 - number)

    if near_100 <= 10 or near_200 <=10:
        return True
    else:
        return False


print(almostthere(104))
print(almostthere(150))
print(almostthere(209))