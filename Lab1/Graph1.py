import numpy as np
x = 1
y1 = np.log(1/(np.e**np.sin(x) + 1)/(5/4 + (1/x)**15))/np.log(1 + x**2)
y_list = []
y_list.append(y1)
x = 10
y2 = np.log(1/(np.e**np.sin(x) + 1)/(5/4 + (1/x)**15))/np.log(1 + x**2)
y_list.append(y2)
x = 1000
y3 = np.log(1/(np.e**np.sin(x) + 1)/(5/4 + (1/x)**15))/np.log(1 + x**2)
y_list.append(y3)

print(y_list)