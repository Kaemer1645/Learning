class Less_Zero(Exception):
    pass

class Triangle:
    def __init__(self, base, side):
        self.base = base
        self.side = side

    def get_field(self):
        if self.base < 0 or self.side < 0:
            raise Less_Zero('Nie moge byc mniejszy od zera')

        return self.base, self.side
try:
    my_example = Triangle(3,-1)
    print(my_example.get_field())

except Less_Zero as message:
    print(message)
