def get_integer(help_text="Give me a number: "):
    return int(input(help_text))


def is_prime_number(number):
    counter = 0
    for my_number in range(2,number+1):
        if my_number % number == 0:
            counter += 1
    if counter == 1:
        print('This is prime number')
    else:
        print('This is not prime number')

number = get_integer()
result = is_prime_number(number)
