listlist = [1,2,5,3]

# use lambda to return numb*2
print(list(map(lambda numbs: numbs ** 2,listlist)))

# use lambda to return even numbs
print(list(filter(lambda numbs: numbs % 2 == 0,listlist)))