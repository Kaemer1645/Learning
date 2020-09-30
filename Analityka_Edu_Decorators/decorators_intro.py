def decorator(func):

    def internal():
        print('Hey! Your Function is inside me!!!')
        return func

    return internal()

#var = decorator(my_func())

@decorator
def my_func():
    hello = 'Hello! I\'m external function'
    print(hello)
my_func()



