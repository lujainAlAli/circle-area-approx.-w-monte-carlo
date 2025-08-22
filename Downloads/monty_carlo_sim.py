import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random as rand
import math
import numpy as np
#monty carlo approximating circle 


radius_circle=20
sqA=(2*radius_circle)**2
dims_square=math.sqrt(sqA)
area_circle_f=math.pi*radius_circle**2

rangeA=-radius_circle
rangeB=radius_circle


def CoordinateFormula(radius,rpts):
    count=0
    shape=''
    colorM=''
    coord_x=np.array(range(rpts))
    coord_y=np.array(range(rpts))
    shape_arr=np.empty(rpts,dtype='<U10')
    colorM_arr=np.empty(rpts,dtype='<U10')
    coord_arr=[coord_x,coord_y,shape_arr,colorM_arr]
    while count<rpts:
        for i in range(rpts):
            x_var=rand.randint(-radius,radius)
            y_var=rand.randint(-radius,radius)
            coord_x[i]=x_var
            coord_y[i]=y_var
            circleEq=x_var**2+y_var**2
            if circleEq<=radius**2:
                shape='circle'
                colorM='green'
            else:
                shape='square'
                colorM='orange'
            colorM_arr[i]=colorM
            shape_arr[i]=shape
        count+=1
    return coord_arr 


coordinate_list=CoordinateFormula(radius_circle,1000)
x_coords=coordinate_list[0]
y_coords=coordinate_list[1]
shape_arr=coordinate_list[2]
color_list=coordinate_list[3]



#graph-quick fix find smth better

ax=plt.gca()
ax.set_xlim(rangeA-20,rangeB+20)
ax.set_ylim(rangeA-20,rangeB+20)
ax.set_aspect('equal')

#circle w/ monte carlo sim

num_inside=(shape_arr=='circle').sum()
num_outside=(shape_arr=='square').sum()
num_points=len(shape_arr)
area_mc_circle=round((num_inside/num_points)*sqA,2)

plt.text(x=-dims_square,y=-dims_square,s='area by monte carlo '+str(area_mc_circle))
plt.text(x=-dims_square,y=-dims_square+10,s='area by formula '+str(area_circle_f))

plt.scatter(x_coords,y_coords,c=color_list,marker='o',s=10)

#square
plt.plot([rangeA,rangeB],[rangeA,rangeA],'b')
plt.plot([rangeA,rangeB],[rangeB,rangeB],'b')
plt.plot([rangeB,rangeB],[rangeA,rangeB],'b')
plt.plot([rangeA,rangeA],[rangeA,rangeB],'b')

# circle w/ geometric formula
circle=plt.Circle((0,0),radius_circle,color='green',fill=False)
fig,ax=plt.subplots()
ax.add_patch(circle)
plt.show()