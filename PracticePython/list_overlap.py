a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,14]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14]

list_without_duplicates = []

for x in a and b:
    if x in a and b:
        list_without_duplicates.append(x)

print(list_without_duplicates)
print((len(a),len(b)))