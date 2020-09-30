def decorator(func):

    def internal(*args, **kwargs):
        print('We decorate function')
        return func(*args, **kwargs)

    return internal




@decorator
def sum_var(a,b,c):
    print('This is simple function, which is sum all variables')
    print(a+b+c)

sum_var(1,2,3)