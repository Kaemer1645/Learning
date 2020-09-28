import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

num_to_string = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

with open('famous_bday.json', 'r') as f:
    json_file = json.load(f)

bday_month = []

for person in json_file:
    split = json_file[person].split('/')
    bday_month.append(num_to_string[int(split[1].lstrip("0"))])

counted = Counter(bday_month)
print(counted)


output_file('plot.html')

month_x = []
count_y = []

for month,count in counted.items():
    if count != 0:
        month_x.append(month)
        count_y.append(count)


x_categories = month_x

p = figure(x_range = x_categories)

p.vbar(x=month_x, top = count_y, width = 0.5)

show(p)