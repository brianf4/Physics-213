import matplotlib.pyplot as plotter
import numpy as np
import os

fig = plotter.figure(figsize=(10, 8))
plot1 = fig.add_subplot(2, 1, 1)

data = np.genfromtxt(os.path.expanduser("~/Documents/spring-2025/physics-213/lab26/rc_circuit_data.csv"), delimiter=',', skip_header=1)

times = np.flip(data[16:34,0])
voltages = data[16:34, 1]

print(voltages)
voltages = np.log(voltages)


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


#plot
linear_regression_data=linear_regression(times, voltages)

print("Thisisyourslope:",linear_regression_data[0])
print("Thisisyourintercept:",linear_regression_data[1])
print("This is your regression coefficient:",linear_regression_data[2])
print("These are your predicted y-values using your model:",linear_regression_data[3])
print("This is your slope error:",linear_regression_data[4])
print("This is your intercept error:",linear_regression_data[5])

plot1.plot(times,voltages,'r+', times, linear_regression_data[3],'b-.')
plot1.set_title("RC Circuit\n$log(V)$ Vs. $t$")
plot1.set_xlabel("$t$ (s)")
plot1.set_ylabel("$log(V)$")
plot1.grid(True)
plot1.minorticks_on()
plot1.set_xlim(1.3) # Set the limits in the x-direction
plot1.legend(["$t$", f"$log(V) = {linear_regression_data[0]:.3f}t + ({linear_regression_data[1]:.3f})$"])

plotter.show()
