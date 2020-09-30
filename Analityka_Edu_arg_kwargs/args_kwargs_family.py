def family(surname, **kwargs):
    print('Our family name is',surname)
    print('Our family member:')
    for key, value in kwargs.items():
        print('Name:',key,' - ','Age:',value)



family('Kowalscy',Adam=33,Halina=57,Marta=22)