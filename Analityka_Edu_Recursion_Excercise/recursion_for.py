#https://analityk.edu.pl/funkcje-rekurencyjne-w-python/

#rozwiązanie z uzyciem for

'''lista = [1,3,7,11,13,17,23]
cel = 17
count = 0
for i in lista:
    if i == cel:
        print("Znalazłem, na pozycji", count)
        break
    else:
        if count == len(lista)-1:
            print("Nie znalazłam celu")
    count+=1'''



#zrobic to samo za pomoca rekurencji



list = [1,3,7,11,17,23]
goal = 23

def recursion_for(list, goal, position):
    print(position)
    if list[position] == goal: print('Znalazlem liczbe na pozycji: '+str(position)); return
    elif list[position] == len(list)-1: print("Nie znalazlem liczby");return
    recursion_for(list,goal, position+1)
    print(position)

recursion_for(list, goal, 0)

print(list[::-1])