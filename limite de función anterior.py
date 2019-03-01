import numpy as np
import matplotlib.pyplot as plt

xmax = 3
n = 50
x = np.linspace(0,xmax,n)

y = [0 for i in range(n)]
for i in range(n):
    y[i]= x[i]**4 - 4*(x[i]**2) - x[i] + 4
    
plt.plot(x,y)
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.ylim(-3,5)
plt.xlim(0,3)
plt.grid()
plt.show()
