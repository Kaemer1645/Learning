sentence = '123_123_123_123_123_123_123'

def recursion(sentence, position):
    if sentence[position] == '1':
        sentence = sentence[0:position] + '7' + sentence[position + 1:]
    elif sentence[position] == '2':
        sentence = sentence[0:position] + '8' + sentence[position + 1:]
    elif sentence[position] == '_':
        pass
    elif sentence[position] == '3':
        sentence = sentence[0:position] + '9' + sentence[position + 1:]
    print(sentence)
    if position == len(sentence) - 1:
        return sentence

    return recursion(sentence, position+1)

print(recursion(sentence,0))
