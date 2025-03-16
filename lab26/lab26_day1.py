import numpy as np
import matplotlib.pyplot as plotter

x = np.array([0.00494, 0.00736, 0.00827, 0.0097, 0.01215, 0.01453, 0.01693, 0.01927, 0.02168, 0.02415, 0.02655, 0.02895, 0.03133, 0.03370, 0.03613, 0.03852, 0.04094, 0.04336, 0.04580, 0.04820])
y = np.array([0.471, 0.715, 0.808, 0.940, 1.193, 1.432, 1.674, 1.908, 2.151, 2.393, 2.632, 2.869, 3.108, 3.345, 3.581, 3.819, 4.057, 4.296, 4.534, 4.771])

x2 = np.array([0.00165, 0.00236, 0.00236, 0.00309, 0.00381, 0.00452, 0.00525, 0.00594, 0.00667, 0.00739, 0.00812, 0.00884, 0.00956, 0.01258, 0.01102, 0.01173, 0.01246, 0.01320, 0.01392, 0.01465])
y2 = np.array([0.465, 0.708, 0.805, 0.952, 1.199, 1.44, 1.691, 1.922, 2.165, 2.413, 2.658, 2.898, 3.139, 3.381, 3.624, 3.866, 4.108, 4.351, 4.593, 4.835])

fig = plotter.figure(figsize=(12, 10))
fig.tight_layout()
plot1 = fig.add_subplot(2, 1, 1)
plot2 = fig.add_subplot(2, 1, 2)

# Plot opitons
plot1.set_title('The Voltage Difference Across a Resistor', family='sans-serif', fontsize=18)
plot1.set_xlabel('$Current (A)$', fontsize=16) # Label for y
plot1.set_ylabel('$Voltage Difference (V)$', fontsize=16) # Label for x
#plot1.set_xlim(1, 3) # Set the limits in the x-direction
#plot1.set_ylim(4, 6) # Set the limits in the y-direction
plot1.grid(True)
plot1.minorticks_on()
plot2.set_title('The Voltage Difference Across a Resistor', family='sans-serif', fontsize=18)
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
