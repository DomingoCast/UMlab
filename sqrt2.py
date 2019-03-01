import numpy as np
import matplotlib.pyplot as plt

n = 5

l = [0 for i in range(n)]

nv=[0 for i in range(n)]

for i in range(n):
    nv[i]=int(i+1)
    
l[0] = 2**0.5
for i in range (1,n):
    l[i] = (2+ l[i-1]**0.5)**0.5

print((2+2**0.5)**0.5)
print((2+(2+2**0.5)**0.5)**0.5)
    
plt.plot(nv,l,".")
plt.xlabel("n")
plt.ylabel("$x_n$")
plt.ylim(0,2)
plt.show()
