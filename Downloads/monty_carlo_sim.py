import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random as rand
import math
import numpy as np
#monty carlo approximating circle 


radius_circle=1000
sqA=(2*radius_circle)**2
dims_square=math.sqrt(sqA)
print("area square" + str(sqA))
area_circle_f=math.pi*radius_circle**2

rangeA=-radius_circle
rangeB=radius_circle


def CoordinateFormula(x_var,y_var,rpts):
    count=0
    coord_x=[]
    coord_y=[]
    shape_list=[]
    colorM_list=[]
    coord_list=[coord_x,coord_y,shape_list,colorM_list]
    while count<rpts:
        x_var=rand.randint(-radius_circle,radius_circle)
        y_var=rand.randint(-radius_circle,radius_circle)
        coord_x.append(x_var)
        coord_y.append(y_var)
        circleEq=x_var**2+y_var**2
        if circleEq<=radius_circle**2:
            shape='circle'
            colorM='green'
        else:
            shape='square'
            colorM='orange'
        colorM_list.append(colorM)
        shape_list.append(shape)
        count+=1
    return coord_list 


coordinate_list=CoordinateFormula(radius_circle,radius_circle,1500000)
x_coords=coordinate_list[0]
y_coords=coordinate_list[1]
shape_list=coordinate_list[2]
color_list=coordinate_list[3]



#graph-quick fix find smth better

#plt.plot([rangeA-radius_circle,rangeB+radius_circle],[rangeA-radius_circle,rangeA-radius_circle],'r')
#plt.plot([rangeA-radius_circle,rangeB+radius_circle],[rangeB+radius_circle,rangeB+radius_circle],'r')
#plt.plot([rangeB+radius_circle,rangeB+radius_circle],[rangeA-radius_circle,rangeB+radius_circle],'r')
#plt.plot([rangeA-radius_circle,rangeA-radius_circle],[rangeA-radius_circle,rangeB+radius_circle],'r')


ax=plt.gca()
ax.set_xlim(rangeA-1000,rangeB+1000)
ax.set_ylim(rangeA-1000,rangeB+1000)
ax.set_aspect('equal')

#circle w/ monte carlo sim

num_inside=shape_list.count('circle')
print(num_inside)
num_outside=shape_list.count('square')
print(num_outside)
print(num_inside/num_outside)
num_points=len(shape_list)
area_mc_circle=(num_inside/num_points)*sqA

plt.text(x=-dims_square,y=-dims_square,s='area by monte carlo '+str(area_mc_circle))
plt.text(x=-dims_square,y=-dims_square+100,s='area by formula '+str(area_circle_f))

plt.scatter(x_coords,y_coords,c=color_list,marker='o')

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