primenumbers_file = open('primenumbers.txt','r')
happynumbers_file = open('happynumbers.txt','r')


with open('overlap_file.txt','w') as f:
    happy_lines_list = []
    prime_lines_list = []
    for prime_lines in primenumbers_file.readlines():
        prime_lines_list.append(int(prime_lines))
        for happy_lines in happynumbers_file.readlines():
            happy_lines_list.append(int(happy_lines))
    overlap = [a for a in happy_lines_list if a in prime_lines_list]
    for line in overlap:
        f.write(str(line)+'\n')


primenumbers_file.close()
happynumbers_file.close()