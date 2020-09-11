# wszystko o klasach w jednym miejscu - jest to plik ukazujący strukture programowania zorientowanego obiektowo


from classtools import AttrDisplay

class Person(AttrDisplay):  # zaczynamy klase z duzej litery

    # pierwsze co bedziemy chcieli stworzyc to bedzie konstruktor klasy, gdy tworzymy klase, kod w inicie jest wykonywany za kazdym razem
    # atrybuty nadaje sie instancjom poprzez przypisanie ich do self w metodzie konstruktora

    def __init__(self, name, job=None,pay=0):  # sugerujemy ze ktos nie bedzie zatrudiony przez wartosc domyslna None (jest to argument opcjonalny)
        # ; gdy juz dla jednego argumentu damy wartosc domyslna,
        # to tak samo musimy postapic dla reszty argumentow
        self.name = name
        self.job = job  # te dane beda dolaczane do instancji jako argumenty. przypisujemy je do self w celu trwalego ich zachowania
        self.pay = pay  # self to nowo utworzony obiekt instancji
        # w przypadku powyzej job jest zmienna lokalna w zakresie funkcji init natomiat self.job jest atrybutem instancji
        # sa to dwie rozne zmienne
        # zapisujemy tutaj referencje job do self.job zeby ja pozniej wywolac w instancji

        # kod dodany w celu hermetyzacji go

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    # przeciazanie operatorow
    #def __str__(self):
        #return ('[Person: %s, Salary: %s]' % (self.name, self.pay))


# jesli chcemy aby przy importowaniu naszego kodu nie byly wyswietlanie funkcje print wbudowane wewnatrz metod to musimy posluzy sie skladnia name - main
# to powoduje ze printy wyswietlanie sa podczas startu testow wewnetrznych a nie przy importowaniu


if __name__ == '__main__':
    marcinek = Person('Marcinek Marcinek Marcinowski')  # instanja klasy Person
    justynka = Person('Justynka', job='geodetka', pay=28123)
    print(justynka)
    # print(marcinek.name,marcinek.job) #wyswietla nam domyslny argument None dla profesji
    # print(justynka.name,justynka.job)
    '''print(marcinek.name.split()[-1])
    justynka.pay*=1.1                           #to samo, zeby tego nie powtarzac i wypisywac za kazdym razem, mozemy sfaktoryzowac (czyli zoptymalizowac utrzymanie kodu i usunac
    powtarzalnosc) nazywa sie to tez hermetyzacja kody, czyli zapisanie danej operacji tylko raz - w tym przypadku usuniemy to z instancji i dodamy jako metode do klasy
    print('%.2f' % (justynka.pay))'''

    # hermetyzacja

    # print(marcinek.lastName(),justynka.lastName())
    # print(justynka)
    # justynka.giveRaise(.20)
    # print(justynka)

    # przeciazanie operatorow

    # w tym przypadku przeciazamy metode __str__ w celu rozszerzenia naszej klasy o wlasny sposob wyswietlania, taki sposob
    # wymieni atrybuty gdy wypiruntuje nasza instancje print(intancja*)

    # dziedziczenie klas - klasa nadrzedna i podrzedna
    # w tym przypadku tworzymy klase podrzedna Manager do klasy nadrzednej Person
    # definiujemy w niej funkcje giveRaise ktora to zgodnie z regula drzewa zastapi nam giveRaise ktore jest w klasie Person

    class Manager(Person):
        def __init__(self, name, pay):
            Person.__init__(self,name,'manager',pay)   #wykonalismy rozszerzenie konstruktora __init__ z klasy nadrzednej Person
        def giveRaise(self,percent,bonus=.10):

            #istnieja dwa sposoby rozszerzania metod

            # zly
            #przeklejenie kodu kopiuj wklej
            #wnetrze metody wyglada wtedy nastepujaco

            #self.pay = int(self.pay * (1 + percent + bonus))

            # sposob bardzo dobry! ktorego nalezy sie trzymac (uzywamy go poniewaz przy zmianie sposobu obliczania podwyzki zmieniamy kod w jednym miejscu
            # w klasie Person a nie w obu w Person i Manager

            Person.giveRaise(self, percent+bonus) #odwolujemy sie wyzej w drzewie

    kowalski=Person('Janusz Kowalski',job='hydraulik',pay=1000)
    #kowalski.giveRaise(.10)
    #print(kowalski.pay)     #kowalski dostaje podwyzke z bonusem +10%
    print(kowalski)

    sebastian=Manager('Sebastian Dreszczynski',pay=10000)


    #polimorfizm w akcji
    for object in (justynka,marcinek,kowalski,sebastian):
        object.giveRaise(0.10)
        print(object)
    #print(sebastian.job)
'''

    # w jaki sposob oprocz dziedziczenia mozna laczyc ze soba klasy?

    # jedna z takich metod jest kompozycja, w tym przypadku za pomoca osadzenia, osadzimy klase Person w Manager

    class Manager:  # nie ma tutaj dziedziczenia - nie jestesmy pod Person w drzewku
        def __init__(self, name, pay):
            self.person = Person(name, 'manager', pay)

        def giveRaise(self, percent, bonus=.10):
            self.person.giveRaise(percent + bonus)

        def __getattr__(self, attr):
            return getattr(self.person, attr)

        def __str__(self):
            return str(self.person) + ' --- manager'
if __name__ == '__main__':
    sebastian = Manager('Sebastian Dreszczynski', pay=10000)
    for object in (justynka, marcinek, sebastian):
        object.giveRaise(0.10)
        print(object)


    # oprocz zastosowania takiej metody moglibysmy rowniez agregowac inne obiekty aby potraktowac je jako zbior

    class Department:
        def __init__(self, *args):
            self.members = list(args)

        def addMember(self, person):
            self.members.append(person)

        def giveRaise(self, percent):
            for person in self.members:
                person.giveRaise(percent)

        def showAll(self):
            for person in self.members:
                print(person)


    development = Department(sebastian, justynka)
    development.addMember(marcinek)
    development.giveRaise(0.1)
    development.showAll()

    # specjalne atrybuty klas pozwalajace nam wyswietlic z jakiej klasy podrzednej pochodzi dana instancja oraz
    #jakie atrybuty zawiera


    print(justynka.__class__.__name__)
    print(sebastian.__class__.__name__)
    print(justynka.__dict__)

    for key in justynka.__dict__:
        print(key, '==>', justynka.__dict__[key])'''
