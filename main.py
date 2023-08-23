import matplotlib.pyplot as plt
import numpy as np
import math

plt.rcParams['font.family'] = ['Microsoft YaHei']
X = [114.5, 123.5, 132.5, 149, 165.5, 182, 198.5, 242.5]
Y = [231.5, 259, 275.6, 297.6, 319.7, 358.3, 374.8, 385.8]
Z = [303.1, 319.7, 352.7, 380.3, 418.9, 446.4, 468.5, 496.0]
W = [534.6, 578.7, 628.3, 677.9, 738.5, 804.7, 843.3, 881.8]

coefficients = np.polyfit(X, Y, 2)
print(coefficients)
# 计算拟合曲线的预测值
predicted_Y = np.polyval(coefficients, X)

# 计算实际数据的平均值
mean_Y = np.mean(Y)

# 计算 SST 和 SSE
SST = np.sum((Y - mean_Y) ** 2)
SSE = np.sum((Y - predicted_Y) ** 2)

# 计算 R-squared 值
R_squared = 1 - (SSE / SST)

print("R-squared:", R_squared)

# 绘制原始数据点和拟合曲线
plt.plot(X, Y, 'rv', label='Data')  # 原始数据点
plt.plot(X, predicted_Y, label='Fitted curve')  # 拟合曲线

Y = Z
coefficients = np.polyfit(X, Y, 2)
print(coefficients)
# 计算拟合曲线的预测值
predicted_Y = np.polyval(coefficients, X)

# 计算实际数据的平均值
mean_Y = np.mean(Y)

# 计算 SST 和 SSE
SST = np.sum((Y - mean_Y) ** 2)
SSE = np.sum((Y - predicted_Y) ** 2)

# 计算 R-squared 值
R_squared = 1 - (SSE / SST)

print("R-squared:", R_squared)

# 绘制原始数据点和拟合曲线
plt.plot(X, Y, 'rv', label='Data')  # 原始数据点
plt.plot(X, predicted_Y, label='Fitted curve')  # 拟合曲线

Y = W
coefficients = np.polyfit(X, Y, 2)
print(coefficients)
# 计算拟合曲线的预测值
predicted_Y = np.polyval(coefficients, X)

# 计算实际数据的平均值
mean_Y = np.mean(Y)

# 计算 SST 和 SSE
SST = np.sum((Y - mean_Y) ** 2)
SSE = np.sum((Y - predicted_Y) ** 2)

# 计算 R-squared 值
R_squared = 1 - (SSE / SST)

print("R-squared:", R_squared)

# 绘制原始数据点和拟合曲线
plt.plot(X, Y, 'rv', label='Data')  # 原始数据点
plt.plot(X, predicted_Y, label='Fitted curve')  # 拟合曲线
# 设置图例和标题
plt.legend()
plt.title('Exponential Curve Fitting')
plt.xlabel("X")
plt.ylabel("Y")

# 显示图形
plt.show()
