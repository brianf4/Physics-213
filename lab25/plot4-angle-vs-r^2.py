import numpy as np
import matplotlib.pyplot as plotter

fig = plotter.figure()
plot4 = fig.add_subplot(111)  
x = [0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15] # r(meters)
y = [7, 5, 6, 8, 12, 6, 3, 7, 8, 8] # angle

xerr = 0.005 # half-step = 0.5cm = 0.005m

yerr = 0.5

r2 = [1 / c**2 for c in x] #creates a new array x^2

xerr2 = []

for num in x:
    xerr2.append(abs(-2 * pow(num, -3) * xerr))

print(xerr2)

#Create a plot of data points only with error bars of the appropriate size. Green points = go
plot4.errorbar(r2, y, yerr, xerr2, fmt='go', capsize=2.5)  

#Creates a plot of line on same plot. Blue dashed = b--
plot4.plot(r2, y, 'b--') 
#See https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
#for full list of plotting formatting options.

csfont = {"fontname": "Times New Roman"} #Changes font
plot4.set_title('angle vs 1 / r^2 (m)', csfont)
plot4.set_xlabel('x - r^2(m)', csfont)
plot4.set_ylabel('y - theta', csfont)

plotter.savefig("plot4-angle-vs-r2.png")

