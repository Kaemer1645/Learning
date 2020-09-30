def multi_arg_kwargs(*args, **kwargs):
    print('Amount of declare args: ',len(args))

    for arg in args:
        print('Value',arg)

    print('Amount of declare kwargs: ',len(kwargs))

    for key, value in kwargs.items():
        print(key, '-->', value)


multi_arg_kwargs(1,2,3,'cat',a=1,b=99,c=4)