import numpy as np
import matplotlib.pyplot as plotter

x = np.array([])
y = np.array([])

x2 = np.array([])
y2 = np.array([])

fig = plotter.figure(figsize=(12, 10))
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
plot2.set_title('The Voltage Difference Across a Resistor in Parallel', family='sans-serif', fontsize=18)
plot2.set_xlabel('$Current (A)$', fontsize=16) # Label for y
plot2.set_ylabel('$Voltage Difference (V)$', fontsize=16) # Label for x
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
linear_regression_data2 = linear_regression(x2, y2)

print("This is your slope", linear_regression_data[0])
print("This is your intercept", linear_regression_data[1])
print("This is your regression coefficient:", linear_regression_data[2])
print("These are your predicted y-values using your model", linear_regression_data[3])
print("This is your slope error:", linear_regression_data[4])
print("This is your intercept error:", linear_regression_data[5])

plot1.plot(x, y, 'r+', x, linear_regression_data[3], 'b-.')
plot2.plot(x2, y2, 'r+', x2, linear_regression_data2[3], 'b-.')


plotter.subplots_adjust(hspace=0.5)
plotter.show()
