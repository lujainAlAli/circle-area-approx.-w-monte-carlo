import matplotlib.pyplot as plt
import numpy as np

from matplotlib.animation import FuncAnimation 

#vector that represents time points
t=np.linspace(0,10,100) #generates an array of a specified number of values evenly spaced within a given interval, including the start and (optionally) the end point
y=np.sin(t)

fig,axis=plt.subplots()

axis.set_xlim([min(t),max(t)])
axis.set_ylim([-2,2])

animated_plot,=axis.plot([],[])

def update_data(frame):
    animated_plot.set_data(t[:frame],y[:frame])
    return animated_plot

animation=FuncAnimation(
                        fig=fig,
                        func=update_data,
                        frames=len(t),
                        interval=25,
                        repeat=True)

animation.save("sine_wave.gif")
plt.show()


