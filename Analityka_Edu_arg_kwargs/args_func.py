def multiple_args(*args):
    print('Amount of declare argument',len(args))
    for arg in args:
        print('Value: ', arg)


multiple_args(3,2,3,3,3)