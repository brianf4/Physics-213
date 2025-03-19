import numpy as np
import matplotlib.pyplot as plotter

x = np.array([3.22754e-04, 4.35181e-04, 5.36011e-04, 6.81152e-04, 7.97485e-04, 9.23462e-04, 0.00107, 0.00120, 0.00133, 0.00145, 0.00160, 0.00173, 0.00186, 0.00200, 0.00213, 0.00228, 0.00242, 0.00258, 0.00285, 0.00299, 0.00314])

y = np.array([1.855, 1.87, 1.88, 1.888, 1.895, 1.903, 1.909, 1.915, 1.919, 1.925, 1.929, 1.933, 1.937, 1.937, 1.944, 1.948, 1.951, 1.952, 1.959, 1.963, 1.964])

fig = plotter.figure(figsize=(10, 8))
plot1 = fig.add_subplot(1, 1, 1)

# Plot opitons
plot1.set_title('The Voltage Difference Across a LED', family='sans-serif', fontsize=18)
plot1.set_xlabel('$Current (A)$', fontsize=16) # Label for y
plot1.set_ylabel('$Voltage Difference (V)$', fontsize=16) # Label for x
#plot1.set_xlim(1, 3) # Set the limits in the x-direction
#plot1.set_ylim(4, 6) # Set the limits in the y-direction
plot1.grid(True)

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

print("This is your slope", linear_regression_data[0])
print("This is your intercept", linear_regression_data[1])
print("This is your regression coefficient:", linear_regression_data[2])
print("These are your predicted y-values using your model", linear_regression_data[3])
print("This is your slope error:", linear_regression_data[4])
print("This is your intercept error:", linear_regression_data[5])

plot1.plot(x, y, 'r+', x, linear_regression_data[3], 'b-.')
plot1.legend(['$\Delta\phi_{led}$', f'y = {linear_regression_data[0]:.2f}x {linear_regression_data[1]:.2f}'])

plotter.show()
