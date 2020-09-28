import json

def user_input():
    what_to_do = input('Please write, what do you want to do: ')
    return what_to_do



def bday_json(file_name):
    with open(str(file_name)+'.json', 'r') as f:
        bday = json.load(f)
        return bday

def add_person(file_name):
    bday = bday_json('famous_bday')
    bday = dict(bday)
    name = input('Please write a name of your person: ')
    bday_date = input('Please write his day of birth: ')
    bday[name] = bday_date
    with open(str(file_name)+'.json', 'r+') as f:
        json.dump(bday, f)


def single_person():
    dictionary = bday_json('famous_bday')
    user_choice = input('Who\'s birthday do you want to look up?')
    bdate = dictionary[user_choice]
    print("{} have got birthday in {}.".format(user_choice,bdate))
    return user_choice

def display_bday_list():
    dictionary = bday_json('famous_bday')
    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for name in dictionary:
        print(name)




def run():
    print('What do you want to do?')
    print('If you would like to: add person - write "add", check list of person - write "check,'
          ' check date of birth of single person - write "single", to exit - write "exit"')
    while True:
        user_do = user_input()
        if user_do == 'add':
            add_person('famous_bday')
        elif user_do == 'check':
            display_bday_list()
        elif user_do == "single":
            single_person()
        elif user_do == 'exit':
            print('')
            print('Thanks for use this program!')
            break




if __name__ == '__main__':
    run()





'''def birthday_dict():
    birthday_dictionary = {"Amadeusz Mozart" : "27/01/1756",
                           "Antonio Vivaldi" : "4/03/1679",
                           "Elizabeth the second" : "21/04/1926"}

    return birthday_dictionary'''

