import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = ['Microsoft YaHei']
num = 30
X = np.linspace(0, 22, num)
Y = [0 for i in range(num)]
Z = [0 for i in range(num)]
W = [0 for i in range(num)]
Y[0] = 0
Z[0] = 5
W[0] = 995
for i in range(num - 1):
    Y[i + 1] = Y[i] + 0.6 * Z[i]
    Z[i + 1] = Z[i] - 0.6 * Z[i] + 0.001407 * Z[i] * W[i]
    W[i + 1] = W[i] - 0.001407 * Z[i] * W[i]
plt.plot(X, Y, marker='o', label='移出者')
plt.plot(X, Z, marker='^', label='已感者')
plt.plot(X, W, marker='v', label='易感者')
plt.xlabel("天数")
plt.ylabel("人数")
# 设置图例和标题
plt.legend()
plt.title('模型')
plt.show()

#
# def fun(x):
#     return 0.0005/(pow(0.05 / 7, x - 1) * 0.00035131 / (0.05 / 7 - 1) - 0.00035131 / (0.05 / 7 - 1))
#
#
# X = np.linspace(1.01, 40, 102)
# Y = [fun(x) for x in X]
# print(fun(10))
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 8))
# ax1.plot(X, Y, color='red', marker='o', linestyle='', markersize=2)
# ax2.plot(X, Y, color='blue', linestyle='-')
# plt.show()
