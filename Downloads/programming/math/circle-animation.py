import matplotlib.pyplot as plt
import numpy as np
from  matplotlib.animation import FuncAnimation
import math


radius=10

degrees=360
limit_adjuster=5

#deg to radians 
for angle in range(degrees):
    radians=angle*np.pi/180

radians=np.linspace(0,4*np.pi,num=100)
xl=radius*np.cos(radians)
yl=radius*np.sin(radians)

#setting up animation
fig,axis=plt.subplots()

axis.set_xlim([min(xl)-limit_adjuster,max(xl)+limit_adjuster])
axis.set_ylim([min(yl)-limit_adjuster,max(yl)+limit_adjuster])

animated_plot,=axis.plot([],[])

def update_circle(frame):
    animated_plot.set_data(xl[:frame],yl[:frame])
    return animated_plot 

animation=FuncAnimation(fig=fig,func=update_circle,frames=len(radians),interval=100)


ax=plt.gca()
ax.set_aspect('equal')


