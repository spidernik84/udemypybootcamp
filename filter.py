def check_even(numbers):
    return numbers % 2 == 0

mynums = [1,2,3,4,5,6]

print(list(filter(check_even,mynums)))
