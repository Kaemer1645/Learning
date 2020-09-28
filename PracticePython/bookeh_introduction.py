from bokeh.plotting import figure, show, output_file



output_file('plot.html')

x = [1,2,3,4,5,6,7]
y = [1,2,3,4,5,6,7]

p = figure()

p.vbar(x=x, top=y, width = 0.5)

show(p)