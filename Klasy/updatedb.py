import shelve

db=shelve.open('persondb')

for key in sorted(db):
    print(key,'\t=>',db[key])

justynka=db['Justynka']
justynka.giveRaise(.10)
db['Justynka']=justynka
print(db['Justynka'])
db.close()
