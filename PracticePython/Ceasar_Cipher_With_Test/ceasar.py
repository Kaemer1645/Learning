#TEST DRIVEN DEVELOPMENT - BASEN ON https://www.youtube.com/watch?v=vgfcnouWe60

import string

def ceasar(word : str, key : int) -> str:
    alphabet = string.ascii_lowercase
    code = alphabet[key:] + alphabet[:key]
    # create tab to convert letter to coded letter, the tab dictionary in keys have got code assigned to letter
    tab = str.maketrans(alphabet, code)
    cipher = word.translate(tab)
    return print(cipher)




szymek = ceasar(word='szymon sleczka',key=5)
szymek_odkodowany = ceasar(word='xedrts xqjhepf',key=-5)




