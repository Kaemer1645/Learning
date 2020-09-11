class PierwszaKlasa:
    def ustawienie(self,dane):
        self.dane=dane
    def wyswietlenie(self):
        print(self.dane)

class DrugaKlasa(PierwszaKlasa):
    def wyswietlenie(self):
        print('To sa moje dane:' +str(self.dane))


class TrzeciaKlasa(DrugaKlasa):
    def __init__(self,value):
        self.data=value
    def __str__(self):
        return self.data

    
x=PierwszaKlasa()
x.ustawienie(10)
x.wyswietlenie()

y=DrugaKlasa()
y.ustawienie(20)
y.wyswietlenie()


z=TrzeciaKlasa('siema')
print(z)
