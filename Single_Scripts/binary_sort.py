def search(array, target):

    left = 0
    right = len(array)
    index = None

    while True:

        index = (left + right) // 2

        if array[index] == target_number:
            print('Your number '+str(array[index])+' is in the list')
            return index
        else:
            if array[index] < target_number:
                left = index + 1
            else:
                right = index
    print('That number doesn\'t exist')
    return -1


A = [1, 3, 4, 5, 7, 9, 11, 15, 16, 17, 19]
target_number = 7
index = search(A, target_number)
