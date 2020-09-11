def write(text = 'Write number of numbers in sequence: '):
    return int(input(text))

def Fibonacci(numbers):
    list = [0,1]
    for x in range(1,numbers):
        list.append(list[x] + list[x-1])
    return print(list)


solv = Fibonacci(write())