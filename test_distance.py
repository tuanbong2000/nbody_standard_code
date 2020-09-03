import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
from numpy.lib.function_base import append
from datetime import datetime
import os, shutil
import sys
import math
# Stars interacting gravitationally

# Anh Tuan Vu

# n is the number of planets
n = 3

path_data_out = "data_out.txt"

# record the data of the stars to arrays from data_out.txt
data = np.loadtxt(path_data_out)
newArray=[]
for j in range(n):
    newArray0 = data[j::n]
    newArray.append(newArray0) 

# print the coordinates of the k-th planet
k=1
print(newArray[k])


def calculateDistance(x,y):  
     dist = math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2+(x[2] - y[2])**2)  
     return dist

for j in range(len(newArray[0])):
    print(calculateDistance(newArray[1][j],newArray[2][j]))



