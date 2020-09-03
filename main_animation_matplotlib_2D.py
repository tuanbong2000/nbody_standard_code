import os, shutil
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
from numpy.lib.function_base import append
from datetime import datetime
from IPython.core.display import Image


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


fig = plt.figure() 
ax1 = plt.axes() 
#ax1 = fig.add_axes((0.06,0.4,0.9,0.6))
color_initial=['r-','b-','g--','c-','m-','k--']
line_lable=['S1','E1','M1','S2','E2','M2']

    
line, = ax1.plot([], [], 'r') 


# lists to store x and y axis points 
xdata, ydata = [], [] 
for j in range(n):
    xdata.append([])
    ydata.append([])
def animate(i):

    # appending new points to x, y axes points list 
    for j in range(n):
        xdata[j].append(newArray[j][i,0])
        ydata[j].append(newArray[j][i,1]) 

    ax1.clear()
    for j in range(n):
        ax1.plot(xdata[j],ydata[j], color_initial[j], linewidth=2, label=line_lable[j])
        ax1.legend(loc='upper right')


    return line,


# The animation of System is recorded on the file animation.gif
ani = animation.FuncAnimation(fig, animate, interval=1, blit=True) 
ani.save('animation.gif', writer='imagemagick', fps=30)
Image('animation.gif')


"""
ani = animation.FuncAnimation(fig, animate, interval=1, blit=True) 
plt.show()

Writer = animation.writers['ffmpeg']
writer = Writer(fps=50, metadata=dict(artist='Me'), bitrate=1800)  #fps tang thi toc do diem tang

anim = animation.FuncAnimation(fig, animate, frames=2000, repeat=True) #frames do dai ngan cua video
anim.save(folder_name + 'starAnimation_%s.mp4' % datetime.now().strftime('%Y-%m-%d %H-%M-%S')
, writer=writer)

path_data_save="/Users/han/Documents/dataTest/"+folder_name1
if not os.path.exists(path_data_save):
        os.makedirs(path_data_save)
#if os.path.exists(path_data_save + folder_name): 
#        shutil.rmtree(path_data_save + folder_name)

shutil.copy("create_data.py",folder_name)
shutil.copy("main_animation_matplotlib_2D.py",folder_name)
shutil.move(folder_name, path_data_save)

"""




