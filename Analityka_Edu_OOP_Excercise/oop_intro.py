#EXC 1

class Book:
    '''title=None
    number_of_pages = None
    author = None
    release_date = None
    owner = None'''
    def __init__(self, title, number_of_pages, author, release_date,owner):
        self.title = title
        self.number_of_pages = number_of_pages
        self.author = author
        self.release_date = release_date
        self.owner = owner

    def informator(self):
        print('Information about your book: \n',('Title: '+ str(self.title), 'Number of pages: ' +str(self.number_of_pages),
                                                 'Author: '+str(self.author),'Release date: '+str(self.release_date),
                                                 'Owner: '+str(self.owner)))
    def new_owner(self, new_owner):
        self.owner = new_owner

LOTR = Book("wladca pierscieni",'130','JRR Tolkien','1980','Jan Kowalski')
LOTR.informator()
new_owner = LOTR.new_owner('Szymon Sleczka')
LOTR.informator()
Jas = Book("Jas",'140','Adnrzej Mucha','1989','Stanislaw Nowak')
Stas = Book("Stas",'65','Bronislaw Komorowski','1989','Andrzej Grodzki')

list = [LOTR,Jas,Stas]

for object in list:
    print(object.informator())


