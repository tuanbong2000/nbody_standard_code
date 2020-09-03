import os, shutil
import sys
import numpy as np
import matplotlib.pyplot as plt
#from create_data import createData
from createPdf import createReport
from datetime import datetime

# Study collision when the corners or mass are changed
# parameters changing the corners of collision are interval_move1 and interval_move2
# parameter changing the mass are interval_move3 

# Input data for all planets in System and create files: data_in.txt, data_info.txt
def createData(path,path_info,object_number,step,i,corner1,corner2):

    # using conver1, corner2 to change the corner of collision
    # using step to change the mass
    # using i to change the object or planet you want to change the mass 
    m=['a1','a2','a3','a4','a5','a6']
    p=['a1','a2','a3','a4','a5','a6']
    v=['a1','a2','a3','a4','a5','a6']

    t = np.zeros(4)
    for j in range(object_number):
        if(j==i):
            t[j]=+step
         
    m[0]= "1" #"%.4s" % str(1+t[0]*0.1)
    p[0]="0 0 0"
    v[0]= "1 %.6s %.6s" % (str(0), str(0))


    m[1]="%.6s" % str(0.003)
    p[1]="0 1 0"
    v[1]="1 %.6s %.6s" % (str(0),str(1))

    m[2]="%.18s" % str(0.037+t[2]*0.0001)
    p[2]="0 1.002 0.001613"
    v[2]="1 %.6s %.6s" % (str(0),str(1.1))

# We use m3-m5 when there are collisions between 2 system 
    m[3]= "1" #"%.4s" % str(1+t[0]*0.1)
    p[3]="6 0 0"
    v[3]= "-1 %.6s %.6s" % (str(corner1), str(t[0]))

    m[4]="%.6s" % str(0.003)
    p[4]="6.016 1 0"
    v[4]="0 %.6s %.6s" % (str(0.2),str(1))

    m[5]="%.12s" % str(0.003)
    p[5]="5.984 1 0"
    v[5]="0 -%.6s %.6s" % (str(0.2),str(1))

# Create data_in.txt
    f= open(path,"w+")
    f.write(str(object_number)+"\n")
    f.write("0\n")
    for j in range(object_number):
        f.write(m[j]+" "+p[j]+ " "+v[j]+"\n")
    f.close() 

# Create data_info.txt
    f1= open(path_info,"w+")
    f1.write("The number of objects: " + str(object_number)+"\n")
    # f1.write("The first star system Sy1\n")
    for j in range(min(object_number,3)):
        f1.write("m%d= " % (j+1) + m[j] +"  p%d=("% (j+1) +p[j]+ ")  v%d= ("% (j+1)+v[j]+")\n")
    
    f1.write("\n")
    if (object_number>3):
        f1.write("The second star system Sy2\n")
        for j in range(3,object_number):
            f1.write("m%d= " % (j+1) + m[j] +"  p%d=("% (j+1) +p[j]+ ")  v%d= ("% (j+1)+v[j]+")\n")
    
    f1.close() 



# We create a Folder to contain all data_input data_output and Reports.
# Folder name
folder_name1="0_mass_total_change//%s//" %(str(datetime.now().strftime("%Y-%m-%d")))
folder_name2=str(datetime.now().strftime("%H-%M-%S"))+"//"
folder_name= folder_name1+folder_name2

# Run C++ to create the file sh nbody_sh1
os.system("g++ -o nbody_sh1 nbody_sh1.C")

# The number of Planets in System
n=3

# using conver1, corner2 to change the corner of collision    
interval_move1=list(range(1))
interval_move2=list(range(1))
for e1 in range(len(interval_move1)): 
        corner1=interval_move1[e1]*0.01
        for e2 in range(len(interval_move2)): 
                corner2=interval_move2[e2]*0.01
                subfolder_name=folder_name+"corner_change_%s//" %(str(e1)+"_"+str(e2))
                if not os.path.exists(subfolder_name):
                        os.makedirs(subfolder_name)
                #shutil.copy("run_animation_3D.py", subfolder_name) #run animation for data_out.txt
                #shutil.copy("run_animation_vpython3D.py",subfolder_name) #run animation for data_out.txt
                path_report_pdf= [subfolder_name+"Report1.pdf",subfolder_name+"Report2.pdf",subfolder_name+"Report3.pdf"]

                for i in range(2,3):  #chose the planet to change mass if i=0 no change, i=1,2,3 change m0,m1,m2
                        interval_move3=list(range(1))
                        for e3 in range(len(interval_move3)): # change the mass of Planet, if step=0 there is no change
                                # using step to change the mass
                                step=interval_move3[e3]
                                # Automatic create data_in
                                path_data_input = subfolder_name+"data_in.txt"
                                path_data_info = subfolder_name+"data_info.txt"
                                createData(path_data_input, path_data_info,n,step,i,corner1,corner2)
                                

                                # Run nbody_sh1, input: data_in.txt, output:data_out.txt
                                path_data_out = subfolder_name+"data_out.txt"
                                step_size_control_parameter = 0.03
                                output_interval = 1
                                total_duration = 20
                                
                                text1 = "./nbody_sh1 -d %s -e 1 -o %s -t %s < " % (str(step_size_control_parameter),str(output_interval), str(total_duration))
                                text2 =path_data_input
                                text3 =" | awk '{print $2, $3, $4}'> "
                                text4 =path_data_out
                                os.system(text1+text2+text3+text4)
                                

                                # Create the first page
                                if(e3==0):
                                        if (os.path.isfile(path_report_pdf[i])):
                                                os.remove(path_report_pdf[i])

                                        file_in_put=open(path_data_info,"r+")
                                        plt.axis('off')
                                        # plt.text(0,1.1,"Bo du lieu on dinh voi 3 vat the ban dau mo phong mat roi, trai dat, mat trang,", color='red')
                                        #plt.text(0,1.05,"khi moon and earth du xa sun, moon quay quanh earth", color='red')
                                        #    plt.text(0,1,"In this data, we consider the same large star systems Sy1 and Sy2.")
                                        #   plt.text(0,0.95,"Each of them includes one Star, one Planet, and one Moon.")
                                        plt.text(0,0.9,"We study the stable and the movement of the star systems with")
                                        plt.text(0,0.85,"step size control parameter d = %s, output interval o= %s and" % (str(step_size_control_parameter), str(output_interval)))
                                        plt.text(0,0.8,"total duration t= %s." % str(total_duration))
                                        #plt.text(0,0.85,"when the mass m"+str(i+4)+ " is variable with step of mass m=%s" % '{:f}'.format(0.1**(2*i+1))+" ", color='blue')
                                        #  plt.text(0,0.75,"Object number n:= 6 ")
                                        # plt.text(0,0.70,"The initial time t:= 0")

                                        plt.text(.1,.20,file_in_put.read())
                                        plt.text(.45,.035,"page 1", color='black')

                                        plt.savefig(path_report_pdf[i])
                                        plt.close()

                                # Plot and create a pdf file
                                # os.system("python3 createPdf.py")   #old version
                                createReport(path_data_info,path_data_out,path_report_pdf[i],e3+2,n)

"""
path_data_save="/Users/han/Documents/dataTest/"+folder_name1
if not os.path.exists(path_data_save):
        os.makedirs(path_data_save)
if os.path.exists(path_data_save + folder_name): 
        shutil.rmtree(path_data_save + folder_name)

"""

shutil.copy("create_data.py",folder_name)
shutil.copy("main_with_total_change.py",folder_name)
#shutil.move(folder_name, path_data_save)



