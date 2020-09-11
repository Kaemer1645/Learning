import random
import string
def write(var = 'Please write type of your password: "weak","medium","strong".'):
    return str(input(var))

def length(key = 'Write length of your password: '):
    return int(input(key))


def password_generator(power, key):
    if power == 'weak':
        password = string.ascii_lowercase
        password = list(password)
        random.shuffle(password)
        pass_print = ''.join(password[:key])
        return print(pass_print)
    if power == 'medium':
        password = string.ascii_letters
        password = list(password)
        random.shuffle(password)
        pass_print = ''.join(password[:key])
        return print(pass_print)
    if power == 'strong':
        password = string.ascii_letters + '1234567890!@#$%^&*()_-[];,.<>/'
        password = list(password)
        random.shuffle(password)
        pass_print = ''.join(password[:key])
        return print(pass_print)



typer = write()
length = length()
generator = password_generator(typer, length)