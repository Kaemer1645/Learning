def decorator(func):

    def internal():
        print('I\'m executes this function:',func.__name__)
        return func

    return internal()



@decorator
def simple_func():
    print('My simple function')



@decorator
def simple_second_func():
    print('My simple function')

simple_func()
simple_second_func()
print('')
simple_func()
