def writer(var = "Write a sentence: "):
    return str(input(var))

def reverse(variable):
    splitter = variable.split()
    rev = " ".join(splitter[::-1])
    return print(str(rev))


solution = writer()
sol2 = reverse(solution)
