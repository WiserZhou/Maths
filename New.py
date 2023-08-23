import math
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Microsoft YaHei'

X = [36, 28, 28, 41, 19, 32, 22, 38, 25, 17, 31, 20, 25, 19, 39, 33, 17, 37, 23, 39]
Y = [192, 113, 88, 294, 28, 123, 51, 252, 56, 16, 141, 32, 86, 21, 231, 187, 22, 205, 57, 265]
Y1 = Y
X1 = [pow(x, 2) for x in X]

# Perform linear regression manually
n = len(X)
sum_X = sum(X1)
sum_Y = sum(Y1)
sum_X_squared = sum(x ** 2 for x in X1)
sum_XY = sum(x * y for x, y in zip(X1, Y1))

a = (n * sum_XY - sum_X * sum_Y) / (n * sum_X_squared - sum_X ** 2)
b = (sum_Y - a * sum_X) / n

# Calculate R-squared value
mean_Y = np.mean(Y1)
SST = np.sum((Y1 - mean_Y) ** 2)
predicted_Y = np.array([a * x + b for x in X1])
SSE = np.sum((np.array(Y1) - predicted_Y) ** 2)
R_squared = 1 - (SSE / SST)

print("Linear Regression:")
print("a:", a)
print("b:", b)
print("R-squared:", R_squared)

# Generate points for the fitted line
X_line = np.linspace(min(X), max(X), 100)
Y_line = a * X_line ** 2 + b

# Perform fitted power curve
N = 2
X2 = [pow(x, N) * y for x, y in zip(X, Y)]
X3 = [pow(x, 2 * N) for x in X]
A = sum(X2) / sum(X3)
print(f"Power curve:({N})")
print("A", A)
# Calculate R-squared value
mean_Y = np.mean(Y)
SST = np.sum((Y - mean_Y) ** 2)
predicted_Y = np.array([A * x ** N for x in X])
SSE = np.sum((np.array(Y) - predicted_Y) ** 2)
R_squared = 1 - (SSE / SST)
print("R-squared:", R_squared)

# Perform polynomial regression using numpy.polyfit
degree = 3  # Set the degree of the polynomial (adjust as needed)
coefficients = np.polyfit(X, Y, degree)
poly = np.poly1d(coefficients)

# Calculate R-squared value
predicted_Y_poly = poly(X)
SSE_poly = np.sum((np.array(Y) - predicted_Y_poly) ** 2)
R_squared_poly = 1 - (SSE_poly / SST)

print("Polynomial Regression (degree", degree, "):")
print("Coefficients:", coefficients)
print("R-squared:", R_squared_poly)

# Generate points for the fitted curve
X_curve = np.linspace(min(X), max(X), 1000)
Y_curve = poly(X_curve)

X_powerLine = np.linspace(min(X), max(X), 1000)
Y_powerLine = [A * x ** N for x in X_powerLine]
# Plotting the data and the regression lines
plt.plot(X, Y, 'rv', label='Data')
plt.plot(X_line, Y_line, label='Linear Regression')
plt.plot(X_curve, Y_curve, label='Polynomial Regression')  # Exponential transformation
plt.plot(X_powerLine, Y_powerLine, label='Power Curve')
# Set legend and labels
plt.legend()
plt.title('Curve Fitting')
plt.xlabel("X")
plt.ylabel("Y")

# Display the plot
plt.show()


