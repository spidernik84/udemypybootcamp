def spygame(numbers):
    
    code = [0,0,7,'x']

    for numb in numbers:
        if numb == code[0]:
            code.pop(0)
    
    return len(code) == 1

print(spygame([0,3,4,2,0,3,6,7,5]))
