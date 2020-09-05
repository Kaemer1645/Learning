from time import strftime
a = input('What is your name? ')
b = input('Enter your age: ')
c = strftime('%Y')
print('You turn 100 year old in: '+ str(int(c)-int(b)+100))
d = input('Please give me number from 0 to 10')
print((str(a)+' ') * int(d))
print('---')
print((str(a)+'\n') * int(d))