

def multiplication_seven(times):
    def internal(func):
        def double_interal(*args, **kwargs):
            response = []
            for _ in range(times):
                solution = 7
                solution = solution * func(*args, *kwargs)
                response.append(solution)
            return response
        return double_interal

    return internal

@multiplication_seven(8)
def func(integer):
    return integer
print(func(7))


#print(multiplication_seven(4)(func)(7))