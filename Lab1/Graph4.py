import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.01)

with plt.xkcd():
    y = input()
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.title(r'$Here_is_what_you_want$')
    plt.plot(x, eval(y))
    plt.show()