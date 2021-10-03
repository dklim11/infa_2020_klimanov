import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [1, 1.42, 1.76, 2, 2.24, 2.5]

plt.errorbar(x, y, xerr = 0.1, yerr = 0.05, linestyle = '')
a, b = np.polyfit(x, y, deg = 1, cov = True)
c, d = np.polyfit(x, y, deg = 4, cov = True)

z = np.arange(0, 8, 0.01)

plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$Approximation$')

plt.plot(z, np.poly1d(c)(z))
plt.plot(z, np.poly1d(a)(z))
plt.grid()
plt.show()