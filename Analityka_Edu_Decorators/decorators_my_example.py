def func(ext):
    print('hello')
    def func2():
        return ext
    return func2()


#a = func(ext(3))

@func
def ext(a):
    return print(2*a)

ext(2)