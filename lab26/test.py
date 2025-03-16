import numpy as np
import matplotlib.pyplot as plotter

fig = plotter.figure()
plot1 = fig.add_subplot(111)

x = [1, 2, 3]
y = [4, 5, 6]

plot1.plot(x, y)
plotter.show()
