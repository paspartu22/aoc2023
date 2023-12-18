import numpy as np

x=np.array([6,6,4,4,6,6,1,1,0,0,2,2,0,0]) 
y=np.array([0,5,5,7,7,9,9,7,7,5,5,2,2,0]) 
i=np.arange(len(x))
#Area=np.sum(x[i-1]*y[i]-x[i]*y[i-1])*0.5 # signed area, positive if the vertex sequence is counterclockwise
Area=np.abs(np.sum(x[i-1]*y[i]-x[i]*y[i-1])*0.5) # one line of code for the shoelace formula
print(Area)