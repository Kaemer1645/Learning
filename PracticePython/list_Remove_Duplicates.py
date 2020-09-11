a = [1,3,3,3,11,35,54,345,123,1223]




def remove_duplicates(variable):
    return print(list(set(variable)))


solution = remove_duplicates(a)


def remove_duplicates_loop(variable):
    without_dup = []
    for element in variable:
        if element not in without_dup:
            without_dup.append(element)

    return print(without_dup)


solution2 = remove_duplicates_loop(a)
