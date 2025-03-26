from logging import warn
import numpy as np
import matplotlib.pyplot as plotter

# total current (I-net)
x = np.array([0.00167, 0.00237, 0.00264, 0.00308, 0.00380, 0.00449, 0.00524, 0.00591, 0.00661, 0.00733, 0.00806, 0.00875, 0.00948, 0.01019, 0.01091, 0.01163, 0.01234, 0.01306, 0.01378, 0.01449])

# c1dc
y1 = np.array([0.471, 0.712, 0.807, 0.866, 1.193, 1.432, 1.680, 1.908, 2.148, 2.392, 2.633, 2.871, 3.110, 3.348, 3.587, 3.826, 4.068, 4.307, 4.544, 4.782])
# c2dc
y2 = np.array([0.002, 0.003, 0.005, 0.005, 0.010, 0.012, 0.016, 0.020, 0.023, 0.027, 0.031, 0.033, 0.038, 0.039, 0.045, 0.048, 0.052, 0.055, 0.058, 0.063])

# potential differene combination
y = y1 + y2


# c1DC Parallel
para_x2 = np.array([0.500, 0.750, 0.850, 1.00, 1.15, 1.25, 1.346, 1.46, 1.50, 1.65, 1.75, 1.85, 2.00, 2.15, 2.35, 2.45, 2.50, 2.65, 2.75])

para_y2= np.array([0.311, 0.465, 0.528, 0.611, 0.704, 0.774, 0.823, 0.893, 0.928, 1.012, 1.079, 1.134, 1.224, 1.318, 1.435, 1.490, 1.523, 1.592, 1.66])


fig = plotter.figure(figsize=(10, 8))
fig.tight_layout()
plot1 = fig.add_subplot(2, 1, 1)
plot2 = fig.add_subplot(2, 1, 2)


# Plot opitons
plot1.set_title('The Voltage Difference Across a Resistor in Series', family='sans-serif', fontsize=18)
plot1.set_xlabel('$Current (A)$', fontsize=16) # Label for y
plot1.set_ylabel('$Voltage Difference (V)$', fontsize=16) # Label for x
#plot1.set_xlim(1, 3) # Set the limits in the x-direction
#plot1.set_ylim(4, 6) # Set the limits in the y-direction
plot1.grid(True)
plot1.minorticks_on()
plot2.set_title('Voltage Difference Across a Resistor in Parallel', family='sans-serif', fontsize=18)
plot2.set_xlabel('$Voltage Difference (V)$', fontsize=16) # Label for y
plot2.set_ylabel('$Current(A)$', fontsize=16) # Label for x
#plot2.set_xlim(1, 3) # Set the limits in the x-direction
#plot2.set_ylim(4, 6) # Set the limits in the y-direction
plot2.grid(True)
plot2.minorticks_on()

def linear_regression(x, y):
    N = len(x)

    if len(x) != len(y):
        print("Your x list is not the same size as your y list")
        print(f'Your x-list is {str(len(x))} long. Your y-list is {str(len(y))} long.')
    elif len(x) <= 2:
        print("Error cannont be calculated for two points or less")

    N = np.size(x)
    x_sum = np.sum(x)
    x_average = x_sum / N
    y_sum =np.sum(y)
    y_average = y_sum / N
    x_devsquared = np.sum((x-x_average)**2) 
    y_devsquared = np.sum((y-y_average)**2) 
    xy_sum = np.sum(x * y)
    xy_dev = np.sum((x-x_average)* (y-y_average))
    xsquared_sum = np.sum(x**2)
    ysquared_sum = np.sum(y**2)
    delta = N * xsquared_sum - (x_sum)**2
    intercept = (xsquared_sum * y_sum - x_sum * xy_sum) / delta
    slope = (N * xy_sum - x_sum * y_sum) / delta
    sigma_y = np.sqrt(np.sum((y-intercept - slope * x)**2) / (N - 2))
    error_intercept = sigma_y * np.sqrt(xsquared_sum / delta)
    error_slope = sigma_y * np.sqrt(N / delta)
    r = xy_dev / np.sqrt(x_devsquared * y_devsquared)
    predictions = intercept + slope * x
    return slope, intercept, r, predictions, error_slope, error_intercept

linear_regression_data = linear_regression(x, y)
linear_regression_data2 = linear_regression(para_x2, para_y2)

print("This is your slope", linear_regression_data[0])
print("This is your intercept", linear_regression_data[1])
print("This is your regression coefficient:", linear_regression_data[2])
print("These are your predicted y-values using your model", linear_regression_data[3])
print("This is your slope error:", linear_regression_data[4])
print("This is your intercept error:", linear_regression_data[5])

plot1.plot(x, y1, 'g+')
plot1.plot(x, y2, 'c+')
plot1.plot(x, y, 'r+', x, linear_regression_data[3], 'b-.')

plot1.legend(['$\Delta\phi_{res1}$', '$\Delta\phi_{res2}$', '$\Delta\phi_{net}$', f'y = {linear_regression_data[0]:.2f}x  {linear_regression_data[1]:.2f}'])

plot2.plot(para_x2, para_y2, 'r+', para_x2, linear_regression_data2[3], 'b-.')

res = 1 / linear_regression_data2[0] 

plot2.legend(['$\Delta\phi_{res, parallel}$', f'y = {linear_regression_data2[0]:.2f}x  {linear_regression_data2[1]:.2f}'])


plotter.subplots_adjust(hspace=0.5)
plotter.show()
