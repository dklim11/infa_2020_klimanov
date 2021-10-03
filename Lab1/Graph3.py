import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.001, 0.001)

y = np.log((x**2 + 1)**np.exp(-abs(x)/10))/np.log(1 + np.tan(1/(1 + np.sin(x)**2)))
 
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$it_is_complicated$')
plt.grid(True)
plt.plot(x, y)
plt.show()