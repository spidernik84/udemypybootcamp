def animal_crackers(text):
    words = text.split()

    if words[0][0].lower == words[1][0].lower:
        return True
    else:
        return False


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
