from abc import ABC, abstractmethod

class Contact(ABC):

    def __init__(self, type, number, name, surname):
        self.type = type
        self.number = number
        self.name = name
        self.surname = surname
        self.friends = []

    @abstractmethod
    def __str__(self):
        pass


class Soldier(Contact):

    def __init__(self,number,name,surname):
        super().__init__('Soldier',number,name,surname)

    def __str__(self):
        info = 'Type: ' + str(self.type) + '\n' + str(self.name) + ' ' + str(self.surname) + '\n'
        info += 'Number: ' + str(self.number) +'\n'
        info += 'Knows: ' + str(self.friends)
        return info