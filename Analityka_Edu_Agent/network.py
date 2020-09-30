import sys
from agent_continue import Soldier

class Network():

    __persons = []
    __authorize = False
    __secretLogin = 'analityk'
    __secretPassword = 'edu.pl'

    def login(func):

        def internal(self, *args, **kwargs):

            if self.__authorize == False:
                print('You must be logged')
                return
            elif self.__authorize == True:
                self.__authorize = False
                return func(self, *args, **kwargs)

        return internal





    def authorize(self):
        login = input('Please write login: ')
        password = input('Please write password: ')

        if login == self.__secretLogin and password == self.__secretPassword:
            print('Authorization was successful')
            return True
        else:
            print('Authorization failed')
            return False

    @login
    def display(self, list):
        [print(i) for i in list]

    @login
    def addPerson(self,number):
        name = input('Name: ')
        surname = input('Surname: ')
        new = Soldier(number, name, surname)
        return new

    @login
    def addColleague(self, persons):
        person_a = int(input('Number of first person: '))
        person_b = int(input('Number of second person: '))

        for p in persons:
            if p.number == person_a:
                p.friends += [person_b]
            if p.number == person_b:
                p.friends += [person_a]

    @login
    def deletePerson(self,list):
        deleter = int(input('Which person would you like to delete? Input number: '))
        for person in list:
            if person.number == deleter:
                list.remove(person)


    def run(self):
        while True:
            print(''
                  '1 - Display list of contacts \n'
                  '2 - Add Person \n'
                  '3 - Add colleagues \n'
                  '4 - Login \n'
                  '5 - Delete Person \n'
                  '9 - Exit program \n')

            x = input('What do you want to do?')

            if x == '1':
                self.display(self.__persons)
            elif x == '2':
                newPerson = self.addPerson(len(self.__persons)+1)
                if newPerson != None: self.__persons.append(newPerson)
            elif x == '3':
                self.addColleague(self.__persons)
            elif x == '4':
                if self.authorize():
                    self.__authorize = True
                else: self.__authorize = False
            elif x == '5':
                self.deletePerson(self.__persons)

            elif x == '9':
                sys.exit()



