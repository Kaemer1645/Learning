word = input('Please write a single word: ')

first_slice = word[0:int(0.5*len(word))]
rev =''.join(reversed(word))
second_slice = rev[0:int(0.5*len(word))]

if first_slice == second_slice:
    print('This world is palindrome')
else:
    print('This is not palindrome')

print(word[::-1])



