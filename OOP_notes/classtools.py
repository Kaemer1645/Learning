#Narzedzie do obslugi klas

#jest to narzedzie ktore udostepnia dziedziczona metode przeciazenia wyswietlania, ktora pokazuje instancje klas z ich nazwami klas, a takze pare
#nazwa=wartosc dla kazdego atrybutu przechowanego w samej instancji (ale nie atrybutow dziedziczonych po klasach)
#mozna ja wmieszac w dowolna klase i bedzie dzialala na dowolnej instancji


class AttrDisplay:

    def gatherAttrs(self):
        attrs=[]
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key,getattr(self,key)))
        return ', '.join(attrs)

    def __str__(self):
        return '[%s: %s]' % (self.__class__.__name__,self.gatherAttrs())

if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count=0
        def __init__(self):
            self.attr1=TopTest.count
            self.attr2=TopTest.count+1
            TopTest.count+=2
    class SubTest(TopTest):
        pass

    X,Y=TopTest(),SubTest()
    print(X)
    print(Y)
    print('koooks')


