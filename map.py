def square(numb):
    return numb ** 2


# option 1 (save in list)
print(list(map(square, [1,3,5,6])))

# option 2 (use in for loop)
for li in map(square,[1,5,10,8]):
    print(li)


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'Even'
    else:
        return mystring[0]

names = ['andy','sally','john']

print(list(map(splicer,names)))