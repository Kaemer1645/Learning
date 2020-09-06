a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


EvenList = []
OddList = []
for even in a:
    if even % 2 == 0:
        EvenList.append(even)
    else:
        OddList.append(even)

print(EvenList)
print('----')
print(OddList)

even_comprehension = [even for even in a if even % 2 == 0]
print('Even '+str(even_comprehension))


