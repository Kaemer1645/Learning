import sys
if len(sys.argv) < 2 or len(sys.argv) > 3:
    print('Program need 2 arguments\nFirst is password \n'
            'Second is direction of new file where you save your passwords. Default password.txt')
    sys.exit()
elif len(sys.argv) == 3:
    file = sys.argv[2]
else:
    file = 'passwords.txt'

list = [sys.argv[1]]


def addNumber(password, number, newList):
    newList.append(password + str(number))
    if number < 9:
        return addNumber(password, number+1, newList)
    else:
        return newList
def changeChar(password,position,newList):
    if password[position].islower():
        new_password = password[0:position] + password[position].upper() + password[position+1:]
        newList.append(new_password)
    if position < len(password)-2: return changeChar(password, position+1, newList)
    else: return newList


def addSpecial(password, position, newList):
    if position < len(password)-1:
        new_password = password[0:position] + '!' + password[position:]
        newList.append(new_password)
        return addSpecial(password, position+1, newList)
    else: return newList

def review(list,position, newList, function):
    newList += function(list[position], 0, [])
    if position < len(list)-1:
        return review(list, position+1, newList, function)
    else: return newList


list = review(list,0,[],addNumber)
list = review(list,0,[],addSpecial)
list = review(list,0,[],changeChar)

print(list)

with open(file,'w') as f:
    f.write('\n'.join(list))






'''listq = ['analityk']
listq = review(listq,0,[],addNumber)
print(listq)
listq = review(listq,0,[],changeChar)
print(listq)'''