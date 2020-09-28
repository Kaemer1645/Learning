from abc import ABC, abstractmethod

class two_wheeler(ABC):
    distance = 0
    def __init__(self, type, engine_capacity, color,mark ,transmission):
        self.type = type
        self.engine_capacity = engine_capacity
        self.color = color
        self.mark = mark
        self.transmission = transmission
    def describe(self):
        print('I\'m',self.type,'My engine is',self.engine_capacity,'. I\'m designed by',self.mark,
              'and my color is',self.color,
              'I have got',self.transmission,'transmission')


    def ride(self):
        self.distance += 1

    @abstractmethod
    def disp_distance(self):
        pass
class motorcycle(two_wheeler):
    def __init__(self, engine_capacity, color,mark ,transmission,max_speed):
        super().__init__("Motorcycle",engine_capacity, color,mark ,transmission)
        self.max_speed = max_speed
    def speed(self):
        print('This is my max speed',self.max_speed)
    def disp_distance(self):
        print('I\'m motorcycle and my distane is',self.distance)

class scooter(two_wheeler):
    def __init__(self, engine_capacity, color, mark, transmission, electric):
        super().__init__("Scooter", engine_capacity, color, mark, transmission)
        self.electric = electric
    def eco(self):
        if self.electric == True:
            print('I\' am eco')
        else:
            print('I\' am not eco.')
    def disp_distance(self):
        print('I\'m scooter and my distane is',self.distance)


'''my_motorcycle = motorcycle('C125','black','honda','automatic','160')
my_motorcycle.describe()
my_motorcycle.speed()
my_motorcycle.ride()
my_motorcycle.ride()
my_motorcycle.ride()
my_motorcycle.disp_distance()'''

'''my_scooter = scooter('C50','yellow','Suzuki','automatic',True)
my_scooter.describe()
my_scooter.eco()'''

database = []
database.append(motorcycle('C125','black','honda','automatic','160'))
database.append(scooter('C50','yellow','Suzuki','automatic',True))
print([x.describe() for x in database])