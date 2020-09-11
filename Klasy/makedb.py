from klasy import Person

marcinek = Person('Marcinek Marcinek Marcinowski')
justynka = Person('Justynka', job='geodetka', pay=28123)



import shelve

db=shelve.open('persondb')
for object in (marcinek,justynka):
    db[object.name]=object
db.close()

import glob
print(glob.glob('person*'))
print(open('persondb.dir').read())
