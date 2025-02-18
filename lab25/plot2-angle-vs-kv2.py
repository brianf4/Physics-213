import numpy as np
import matplotlib.pyplot as plotter

fig = plotter.figure()
plot2 = fig.add_subplot(111) # angle vs kv^2

x = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0, 5.25, 5.5, 5.75, 6.0] # kv
y = [0, 7, 8, 10, 17, 22, 24, 28, 26, 29] # angle

xerr = 0.05 #(angle) Different Error bar corresponding to each x-value

yerr = 0.5

xerr2 = []  

for num in x:
    xerr2.append(2 * num * xerr)

kv2 = [c**2 for c in x]
#Create a plot of data points only with error bars of the appropriate size. Green points = go
plot2.errorbar(kv2, y, yerr, xerr2, fmt='go', capsize=2.5)  

#Creates a plot of line on same plot. Blue dashed = b--
plot2.plot(kv2, y, 'b--') 
#See https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
#for full list of plotting formatting options.

csfont = {"fontname": "Avenir Next"} #Changes font
plot2.set_title('angle vs kv^2', csfont)
plot2.set_xlabel('x', csfont)
plot2.set_ylabel('y', csfont)

plotter.savefig("plot2-angle-vs-kv^2.png")

