#OOP Excercise
from abc import ABC, abstractmethod

class Bird:
    def __init__(self,type,velocity):
        self.type = type
        self.velocity = velocity
    def fly(self):
        print('Here ',self.type, '. Soon i start my flight and i get',self.velocity,' km per/hour')
    @abstractmethod
    def get_a_noise(self):
        pass


class Eagle(Bird):
    def __init__(self, velocity):
        super().__init__('Orzel',velocity)
    def hunting(self):
        print('Here',self.type,'. I started hunting.')
    def get_a_noise(self):
        print('trriiii')



class Penguin(Bird):
    def __init__(self, velocity):
        super().__init__('Pingwin',velocity)
    def skid(self):
        print('Here',self.type,'I started skidding.')
    def fly(self):
        print('Here',self.type,'I can\'t fly :(')
    def get_a_noise(self):
        print('krrrr')


eagle = Eagle(80)
eagle.fly()
eagle.hunting()
eagle.get_a_noise()
print('')
penguin = Penguin(20)
penguin.fly()
penguin.skid()
penguin.get_a_noise()