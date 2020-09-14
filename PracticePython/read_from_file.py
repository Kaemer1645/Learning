'''student_scores = {'Adama': 100, 'Starbuck': 75, 'Apollo': 80, 'Athena': 85, 'Agathon': 90}
for items in student_scores.keys():
    print(items)'''

'''file_name = 'nameslist.txt'
doc = {'Lea':0,'Luke':0,'Darth':0}
with open(file_name,'r') as file:
    for line in file.readlines():
        if line.strip() == 'Lea':
            #print('kot')
            lea_score = doc['Lea']
            lea_score += 1
            doc['Lea'] = lea_score
        elif line.strip() == 'Luke':
            luke_score = doc['Luke']
            luke_score += 1
            doc['Luke'] = luke_score
        if line.strip() == 'Darth':
            darth_score = doc['Darth']
            darth_score += 1
            doc['Darth'] = darth_score

print(doc.items())'''


# : extra

'''file_name = 'Training_01.txt'
doc = {}
with open(file_name,'r') as f:'''



counter_dict = {}
with open('Training_01.txt') as f:
	line = f.readline()
	while line:
		line = line[3:-26]
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print(counter_dict)