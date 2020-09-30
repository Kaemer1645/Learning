sentence = 'I like programming in Python'



def letter_count(text):
    word = 1
    letters = 0
    letter_counter = {}
    for letter in text:
        if letter == ' ':
            word += 1
        else:
            letters += 1
            if letter in letter_counter:
                letter_counter[letter] +=1
            else:
                letter_counter[letter] = 1


    return print('Word:', word, 'Letter:', letters, 'Letter counter:',letter_counter)

var = letter_count(sentence)