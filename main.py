numbers = [2, 2, 456, 420, 69, 69, 55, 55, 234]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
