# return a list of even numbers in a list

mylist = []

def myfunc(*args):
    mylist = [item for item in args if item%2 == 0]
    return mylist

print(myfunc(5,6,10,20))