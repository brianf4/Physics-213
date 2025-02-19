import numpy as np
import matplotlib.pyplot as plotter

fig = plotter.figure()
plot3 = fig.add_subplot(111)  
x = [0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15] # r(meters)
y = [7, 5, 6, 8, 12, 6, 3, 7, 8, 8] # angle

xerr = 0.005 # half-step = 0.5cm = 0.005m

yerr = 0.5


#Create a plot of data points only with error bars of the appropriate size. Green points = go
plot3.errorbar(x, y, yerr, xerr, fmt='go', capsize=2.5)  

#Creates a plot of line on same plot. Blue dashed = b--
plot3.plot(x, y, 'b--') 
#See https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
#for full list of plotting formatting options.

csfont = {"fontname": "Times New Roman"} #Changes font
plot3.set_title('angle vs r (m)', csfont)
plot3.set_xlabel('x - r(m)', csfont)
plot3.set_ylabel('y - theta', csfont)

plotter.savefig("plot3-angle-vs-r.png")

