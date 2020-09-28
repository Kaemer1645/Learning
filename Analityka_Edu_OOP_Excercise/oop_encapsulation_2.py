#exc2


class Building:
    def __init__(self):
        self.is_empty = True
        self.person_in = 0
    def entry(self):
        self.person_in += 1
        if self.person_in > 0:
            self.is_empty = False
    def out(self):
        self.person_in -= 1
        if self.person_in == 0:
            self.is_empty = True

        if self.person_in == -1:
            print('It could\'t be less than zero people in building')
            self.person_in += 1
    def check(self):
        if self.is_empty == True:
            print('Building is empty')
        else:
            print('Budynek isn\'t empty')




if __name__ == '__main__':
    inst = Building()
    inst.check()
    inst.entry()
    inst.check()
    inst.out()
    inst.check()
    inst.out()
