list = [1,2,3,'123',55,4]

def recurtion_count(list, position, amount):
    if position == len(list): return print(amount)
    if type(list[position]) == int: return recurtion_count(list, position+1, amount+1)
    else: return recurtion_count(list,position+1,amount)


recurtion_count(list,0,0)