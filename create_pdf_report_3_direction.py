from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import numpy  as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.font_manager as font_manager

# Input data is data_in.txt. We will create a Report1.pdf which describe movements of a System with 3 directional projections 

# Set the font properties (can use more variables for more fonts)
#font_path = 'C:\Windows\Fonts\AGaramondPro-Regular.otf'
font_prop = font_manager.FontProperties(size=7)  #+fname=font_path


# Merge all pdf-files in paths
def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

# Create a file data_info from data_in
def create_data_info(path_data_in,path_data_info):
    f2= open(path_data_info,"w+")
        
    f1 = open(path_data_in,"r")
    # The number of objects
    line = f1.readline()
    number_object=int(line[0])
    f2.write("The number of objects: "+str(number_object)+"\n")

    #The initial time
    line = f1.readline()
    f2.write("The initial time: "+line)
        
    for i in range(number_object):
        line = f1.readline()
        line_split=line.split()
        f2.write("Planet %d: " %(i+1))
        f2.write("m%d="%(i+1) +line_split[0]+" ")
        f2.write("p%d=("%(i+1) +line_split[1]+","+line_split[2]+","+line_split[3]+")"" ")
        f2.write("v%d=("%(i+1) +line_split[4]+","+line_split[5]+","+line_split[6]+")""\n")
    f2.close

# Each figure is Two-dimensional graph. We create data for points in Two-Dimensional Coordinate Systems.
def create_data_out_x(path_data_input,path_data_out,step,time):
        # Run nbody_sh1 to create output data, input: data_in.txt, output:data_out.txt
        text1 = "./nbody_sh1 -d 0.03 -e 1 -o %.4s -t %s < " % (step, time)
        text2 =path_data_input
        text3 =" | awk '{print $3, $4}'> "
        text4 =path_data_out
        os.system(text1+text2+text3+text4)
def create_data_out_y(path_data_input,path_data_out,step,time):
        # Run nbody_sh1 to create output data, input: data_in.txt, output:data_out.txt
        text1 = "./nbody_sh1 -d 0.03 -e 1 -o %.4s -t %s < " % (step, time)
        text2 =path_data_input
        text3 =" | awk '{print $2, $4}'> "
        text4 =path_data_out
        os.system(text1+text2+text3+text4)
def create_data_out_z(path_data_input,path_data_out,step,time):
        # Run nbody_sh1 to create output data, input: data_in.txt, output:data_out.txt
        text1 = "./nbody_sh1 -d 0.03 -e 1 -o %.4s -t %s < " % (step, time)
        text2 =path_data_input
        text3 =" | awk '{print $2, $3}'> "
        text4 =path_data_out
        os.system(text1+text2+text3+text4)

#createReport with the information of alle Planets
def createReport(path_data_info,path_data_out,path_report_pdf,n):
    
    data = np.loadtxt(path_data_out)
    newArray=[]
    # Plot for 6 Object
    for j in range(n):
        newArray1 = data[j::n]
        newArray.append(newArray1) 

    # Create a pdf file
    color_initial=['b*','g*','r*','c*','m*','k*']
    color=['b-','g-','r--','c-','m-','k--']
    color_figure=['blue','green','red','cyan','magenta','black']
    line_lable=['S1','E1','M1','S2','E2','M2']


    fig = plt.figure()
    ax1 = fig.add_axes((0.085,0.3,0.85,0.65))

    for j in range(n):
        ax1.plot(newArray[j][0,0],newArray[j][0,1], color_initial[j])
    for j in range(n):
        ax1.plot(newArray[j][:,0],newArray[j][:,1], color[j], label=line_lable[j])
        ax1.legend(loc='upper right', prop=font_prop)  

    file_in_put=open(path_data_info,"r+")
    lineList=file_in_put.readlines()
    for j in range(min(n,3)):
        fig.text(.05,.15-j*0.05,lineList[j+2], color=color_figure[j], fontproperties=font_prop)
    
    if (n>3):
       for j in range(n-3):
           fig.text(.5,.15-j*0.05,lineList[j+5], color=color_figure[j+3], fontproperties=font_prop)


    fig.savefig('data.pdf')
    plt.close()

    if os.path.isfile(path_report_pdf):
        paths = [path_report_pdf,'data.pdf']
        merge_pdfs(paths, output=path_report_pdf)
    else: 
        os.rename(r'data.pdf', r'%s' %(path_report_pdf))

#createReport without the information of alle Planets
def createReport2(path_data_info,path_data_out,path_report_pdf,n):
    
    data = np.loadtxt(path_data_out)
    newArray=[]
    # Plot for 6 Object
    for j in range(n):
        newArray1 = data[j::n]
        newArray.append(newArray1) 

    # Create a pdf file
    color_initial=['b*','g*','r*','c*','m*','k*']
    color=['b-','g-','r--','c-','m-','k--']
    color_figure=['blue','green','red','cyan','magenta','black']
    line_lable=['S1','E1','M1','S2','E2','M2']


    fig = plt.figure()
    ax1 = fig.add_axes((0.085,0.15,0.85,0.8))

    for j in range(n):
        ax1.plot(newArray[j][0,0],newArray[j][0,1], color_initial[j])
    for j in range(n):
        ax1.plot(newArray[j][:,0],newArray[j][:,1], color[j], label=line_lable[j])
        ax1.legend(loc='upper right', prop=font_prop)  

    fig.savefig('data.pdf')
    plt.close()

    if os.path.isfile(path_report_pdf):
        paths = [path_report_pdf,'data.pdf']
        merge_pdfs(paths, output=path_report_pdf)
    else: 
        os.rename(r'data.pdf', r'%s' %(path_report_pdf))

#create the main Report-Report1.pdf
def create_pdf_3_direction(path_data_in,path_data_info, path_data_out,path_report_pdf,step,time):
    create_data_info(path_data_in,path_data_info)

    #create the page 1 with the information of alle Planets
    create_data_out_x(path_data_in, path_data_out,step,time)
    createReport(path_data_info,path_data_out,path_report_pdf,number_object)

    #create the page 2 without the information of alle Planets
    create_data_out_y(path_data_in, path_data_out,step,time)
    createReport2(path_data_info,path_data_out,path_report_pdf,number_object)

    #create the page 3 without the information of alle Planets
    create_data_out_z(path_data_in, path_data_out,step,time)
    createReport2(path_data_info,path_data_out,path_report_pdf,number_object)



path_data_in="data_in.txt"
path_data_out="data_out.txt"
path_data_info="data_info.txt"        
path_report_pdf = "Report1.pdf"


#output interval o
output_interval = 0.1
#total duration t
total_duration = 50
read_txt = open(path_data_in,'r')

# The number of planets in the System
number_object = int(read_txt.read(1)) 

# Create Report1.pdf
create_pdf_3_direction(path_data_in,path_data_info, path_data_out,path_report_pdf,output_interval,total_duration)
