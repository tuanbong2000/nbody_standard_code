from vpython import *
import os, shutil
import sys
import numpy as np
from datetime import datetime

# Stars interacting gravitationally

# Anh Tuan Vu
       
# Run C++ to create the file sh nbody_sh1
os.system("g++ -o nbody_sh1 nbody_sh1.C")
    
# Run nbody_sh1 to create output data, input: data_in.txt, output:data_out.txt
path_data_input ="data_in.txt"
path_data_out = "data_out.txt"

text1 = "./nbody_sh1 -d 0.03 -e 1 -o 0.1 -t 50 < "
text2 =path_data_input
text3 =" | awk '{print $2, $3}'> "
text4 =path_data_out
os.system(text1+text2+text3+text4)

#number_object 
read_txt = open('./'+path_data_input,'r')
n = int(read_txt.read(1)) #read_txt[0,0]

# record the data of the stars to arrays from data_out.txt
data = np.loadtxt(path_data_out)
newArray=[]
# Plot for n Objects
for j in range(n):
    newArray0 = data[j::n]
    newArray.append(newArray0) 

step = len(newArray[0][:,0])

#VPython to simulation star system.

s = 'Test of <b><i>graphing</i></b>. Move the mouse over the graph to explore its interactivity.'
s += '<br>Drag a rectangle in the graph to zoom. Examine the icons at the upper right.'
s += '<br>Click the "Reset axes" icon to restore. Drag along the bottom or left to pan.'
oscillation = graph(title=s, xtitle='time', ytitle='value', fast=False, width=800)

color_initial=[color.red,color.blue,color.green,color.cyan,color.magenta,color.black]
star_name=["S1","E1","M1","S2","E2","M2"]
funct=[]
for i in range(n):
    funct0 = gcurve(color= color_initial[i], width=2, markers=False, marker_color=color_initial[i], label=star_name[i])
    #funct0 = gdots(color=color_initial[i], size=0.001, label=star_name[i])
    funct.append(funct0)

for j in range(step):
    rate(50)
    for i in range(n):
        funct[i].plot(newArray[i][j,0],newArray[i][j,1])
