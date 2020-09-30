#zapisac to za pomoca rekurencji

'''    def search (array, target):

        left = 0
        right = len(array)
        index = 0

        while left < right:

            index = (left + right) // 2

            if array[index]==target_number:
                return index
            else:
                if array[index]<target_number:
                    left = index+1
                else:
                    right = index

        return -1

    A = [1,3,4,5,7,9,11,15,16,17,19]
    target_number = 8
    index = search(A, target_number)
    print (index)'''

A = [1,3,4,5,7,9,11,15,16,17,19]
B = 17

def recursion_binary(list, start, end, goal):
    if start>end:return False
    drop = (start + end) // 2

    if list[drop] == goal:
        print('I find your number on postion: '); return drop
    elif list[drop] < goal:return recursion_binary(list, drop + 1, end, goal)
    elif list[drop] > goal:return recursion_binary(list, start, drop -1, goal)

print(recursion_binary(A,0,len(A)-1,B))