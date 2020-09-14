def write(var = 'Please input a number: '):
    return int(input(var))


def searcher(variable):
    list_of_numbers = []
    print('If you want to stop the function, write 000: ')
    while True:
        if variable not in list_of_numbers:
            list_of_numbers.append(variable)
        else:
            print(True)
        variable = write()
        if variable == 000:
            break
        list_of_numbers.sort()

    print(list_of_numbers)

def run():
    element_searcher = searcher(write())
    return element_searcher



if __name__ == '__main__':
    run()