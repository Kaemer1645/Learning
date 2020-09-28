



'''def maxer(a = input("Put first variable here"),b = input("Put second variable here"),c = input("Put third variable here")):
    list = [a,b,c]
    list.sort()
    return print(list[-1])

a = maxer()'''



# or

def maxer(a = input("Put first variable here"),b = input("Put second variable here"),c = input("Put third variable here")):
    if a > b and a > c:
        print('Maximum value is '+str(a))
    elif b > a and b > c:
        print('Maximum value is ' + str(b))
    elif c > a and c > b:
        print('Maximum value is ' + str(c))

a = maxer()
