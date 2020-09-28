import random as rd

#open file
def word_random():
    with open('sowpods.txt','r') as f:
        lines = f.readlines()
        randomek = rd.choice(lines)
        randomek = randomek.strip()
        return randomek




def guess_word():
    win = 0
    print('Welcome to HANGMAN :) ')
    word = word_random()
    #word = 'KOT'
    print('_ '*len(word))
    flat = list('_' * len(word))
    count = 0
    guess_to_win = 6
    while win == 0:
        letter = input('Guess your letter: ')
        if letter in word.lower():
            position = ([pos for pos, char in enumerate(word.lower()) if char == letter])
            if len(position) > 1:
                for x in position:
                    flat[x] = letter
            else:
                flat[position[0]] = letter
        else:
            count += 1
            print('You have got ' + str(guess_to_win-count) + ' incorrect guesses left')
        if '_' not in flat and guess_to_win - count > 0:
            print('You win')
            break
        elif guess_to_win - count <= 0:
            print('You loose')
            break
        print(' '.join(flat))






def run():
    function = guess_word()

if __name__ == '__main__':
    run()