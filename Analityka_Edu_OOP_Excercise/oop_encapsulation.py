#EXC 1

class car:
    def __init__(self):
        self.__engine = False
        self.__gear = 0
        self.__speed = 0

    def turn_on(self):
        self.__engine = True

    def turn_off(self):
        self.__engine = False

    def __next_gear(self):
        if self.__gear <= 6: self.__gear +=1; print(self.__gear)

    def __previous_gear(self):
        if self.__gear >= 0: self.__gear -=1; print(self.__gear)

    def speed_up(self):
        if self.__engine == True:
            self.__speed += 10
            print(self.__speed)
            self.__next_gear()

    def brake(self):
        if self.__speed >= 0:self.__speed -= 10
        else: self.__speed = 0
        print(self.__speed)
        self.__previous_gear()
if __name__ == '__main__':

    inst = car()
    inst.turn_on()
    inst.speed_up()
    inst.speed_up()
    inst.brake()
    inst.brake()
    inst.turn_off()



