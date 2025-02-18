import numpy as np
import matplotlib.pyplot as plotter

fig = plotter.figure()
plot1 = fig.add_subplot(111) # angle vs kv

x = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0, 5.25, 5.5, 5.75, 6.0] # kv
y = [0, 7, 8, 10, 17, 22, 24, 28, 26, 29] # angle

xerr = 0.05 #(angle) Different Error bar corresponding to each x-value

yerr = 0.5

#Create a plot of data points only with error bars of the appropriate size. Green points = go
plot1.errorbar(x, y, yerr, xerr, fmt='go', capsize=2.5)  

#Creates a plot of line on same plot. Blue dashed
#= b--
plot1.plot(x, y, 'b--') 
#See https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
#for full list of plotting formatting options.

csfont = {"fontname": "Avenir Next"} #Changes font
plot1.set_title('Angle vs Kv', csfont)
plot1.set_xlabel('x', csfont)
plot1.set_ylabel('y', csfont)

plotter.savefig("plot1-angle vs kv.png")




