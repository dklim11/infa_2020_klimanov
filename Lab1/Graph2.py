import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.01, 0.01)

plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$f(x) = x^2 - x - 6$')
plt.plot(x, x**2 - x - 6)
plt.grid(True)
plt.xticks(np.linspace(-10, 10, 20))
plt.xticks(rotation = 30)
plt.yticks(rotation = 40)
plt.yticks(np.linspace(-10, 100, 22))
plt.show()