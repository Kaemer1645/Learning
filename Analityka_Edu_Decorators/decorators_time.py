import time

def decorator(func):

    def internal(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        x = func(*args,**kwargs)
        end = time.time()
        print(end - start)
        return x
    return internal

@decorator
def my_func(**kwargs):
    for x,y in kwargs.items():
        print(x, y)

my_func(a=1,b=2,c=3)