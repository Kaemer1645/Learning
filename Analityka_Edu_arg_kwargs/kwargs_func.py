def multiple_kwargs(**kwargs):
    print('Amount of declare arguments',kwargs)

    for key, value in kwargs.items():
        print(key, '-->', value)


multiple_kwargs(a=1,b=2,c=55)