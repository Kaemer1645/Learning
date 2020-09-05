x = int(input('Please write a number: '))
for number in range(2, x+1):
    if x % number == 0:
        print(number)