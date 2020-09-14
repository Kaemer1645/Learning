#cows and bulls game
import random as rd


def writer(write_var = 'Please write a correct 4 digit code to gain a cows: '):
    inx = int(input(write_var))
    write_digit = [int(number) for number in str(inx)]
    print(write_digit)
    return write_digit


def run(comparison):
    code = rd.randint(1000,9999)
    code_digit = [int(number) for number in str(code)]
    print(code_digit)
    cows = 0
    while code_digit != comparison:
        for x in code_digit:
            if comparison[0] == x:
                cows += 1
            elif comparison[1] == x:
                cows += 1
            elif comparison[2] == x:
                cows += 1
            elif comparison[3] == x:
                cows += 1
        if cows == 0:
            print('You have got 4 bulls :(')
            print('You have got 0 cows :)')
        elif cows == 1:
            print('You have got 3 bulls :(')
            print('You have got 1 cows :)')
        elif cows == 2:
            print('You have got 2 bulls :(')
            print('You have got 2 cows :)')
        elif cows == 3:
            print('You have got 1 bulls :(')
            print('You have got 3 cows :)')
        cows = 0
        comparison = writer()
        if code_digit == comparison:
            print('You have got 0 bulls :(')
            print('You have got 4 cows :)')
            print('Congratulations, you Win :)')

if __name__ == '__main__':
    sol2 = run(comparison=writer())