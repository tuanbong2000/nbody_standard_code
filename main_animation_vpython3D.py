from vpython import *
import os, shutil
import sys
import numpy as np

# Stars interacting gravitationally

# Anh Tuan Vu


# Run C++ to create the file sh nbody_sh1
os.system("g++ -o nbody_sh1 nbody_sh1.C")
    
# Run nbody_sh1 to create output data, input: data_in.txt, output:data_out.txt
path_data_input ="data_in.txt"
path_data_out = "data_out.txt"

text1 = "./nbody_sh1 -d 0.03 -e 1 -o 0.1 -t 50 < "
text2 =path_data_input
text3 =" | awk '{print $2, $3, $4}'> "
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


giant=[]
color_initial=[color.red,color.blue,color.green,color.cyan,color.magenta,color.yellow]

scene.caption = """In GlowScript programs:
To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""
for j in range(n):
        
        giant0 = sphere(pos=vector(newArray[j][0,0],newArray[j][0,1],newArray[j][0,2]), radius=1e-3, color=color_initial[j], 
                        make_trail=True, trail_type='points', interval=1, retain=500) 
                        # retain la cai duoi, radius phai chon dung tuong thich voi quy dao di chuyen, interval la khoang danh dau point, make_trail la co duoi hay ko.
        giant.append(giant0)

i=1
while (i<step):
        rate(100)
        for j in range(n):
                
                # Save all iteration of move
                """
                giant[j] = sphere(pos=vector(newArray[j][i,0],newArray[j][i,1],newArray[j][i,2]), radius=2e-2, color=color_initial[j], 
                                make_trail=False, trail_type='points', interval=1000, retain=1)
                """

                giant[j].pos = vector(newArray[j][i,0],newArray[j][i,1],newArray[j][i,2]) 
                
        
        i +=1
