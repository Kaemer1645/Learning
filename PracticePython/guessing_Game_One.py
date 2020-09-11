import random
number = None
number_random = random.randint(1,9)
while number != number_random:
    number = int(input('Please write number between 1 and 9: '))
    if number > number_random:
        print('Your number is higher than my number')
    elif number < number_random:
        print('Your number is smaller than my number')
    else:
        print('Your number is exactly the same as my number')
