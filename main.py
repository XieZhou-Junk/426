import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

plt.figure(figsize=(9, 9))

x = np.linspace(-3, 3, 1000)
X = np.array([0, 1, 2, 3, -1, -2, -3])
Y = np.array([-1.22, 1.85, 3.22, 10.29, 2.21, 3.72, 8.7])


def f(p):
    a, b, c = p
    return Y - (a + b * X + c * X ** 2)


r = leastsq(f, [1, 1, 1])
a, b, c = r[0]
print("a=", a, "b=", b, "c=", c)

plt.scatter(X, Y, s=100, alpha=1.0, marker='o', label='数据点')

y = a + b * x + c * x ** 2

ax = plt.gca()

ax.set_xlabel(..., fontsize=20)
ax.set_ylabel(..., fontsize=20)
# 设置坐标轴标签字体大小

plt.plot(x, y, color='r', linewidth=5, linestyle=":", markersize=20, label='拟合曲线')

plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize='xx-large')

plt.xlabel('安培/A')
plt.ylabel('伏特/V')
xlim = x.max() * 0.1
ylim = y.max() * 0.1
plt.xlim(x.min() - xlim, x.max() + xlim)
plt.ylim(y.min() - ylim, y.max() + ylim)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
# 刻度字体大小
plt.legend(loc='upper left')

plt.show()
