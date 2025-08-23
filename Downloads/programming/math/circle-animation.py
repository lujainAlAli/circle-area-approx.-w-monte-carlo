import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation 
import math


r=20
h=0
b=0
x=np.linspace(-r,r,5)
y=-np.sqrt(r**2-(x-h)**2)+b
z=np.sqrt(r**2-(x-h)**2)+b
fig,axis=plt.subplots()

print(y)

axis.set_xlim([min(x),max(x)])
axis.set_ylim(int(min(y)),int(max(y)))


axis.plot(x,y,z)
plt.show()