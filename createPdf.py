
# Use numpy and matplotlib.pyplot to plot from file txt
import os
import numpy  as np
import matplotlib.pyplot as plt
from addPdfPage import merge_pdfs # Edit pdf
from matplotlib.animation import FuncAnimation
import matplotlib.font_manager as font_manager

# Set the font properties (can use more variables for more fonts)
#font_path = 'C:\Windows\Fonts\AGaramondPro-Regular.otf'
font_prop = font_manager.FontProperties(size=7)  #+fname=font_path



def createReport(path_data_info,path_data_out,path_report_pdf,page_number,n):
    
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
    ax1 = fig.add_axes((0.1,0.3,0.85,0.65))
#    ax1.set_xlim(-50,50)
#   ax1.set_ylim(-50,50)

    for j in range(n):
        ax1.plot(newArray[j][0,0],newArray[j][0,1], color_initial[j])
    for j in range(n):
        ax1.plot(newArray[j][:,0],newArray[j][:,1], color[j], label=line_lable[j])
        ax1.legend(loc='upper right', prop=font_prop)  

    file_in_put=open(path_data_info,"r+")
    lineList=file_in_put.readlines()
#    fig.text(.05,.34,lineList[0], color='black')
    #fig.text(.05,.2,lineList[1], color='black', fontproperties=font_prop)
    for j in range(min(n,3)):
        fig.text(.05,.15-j*0.05,lineList[j+1], color=color_figure[j], fontproperties=font_prop)
    
    if (n>3):
        fig.text(.5,.2,lineList[6], color='black', fontproperties=font_prop)
        for j in range(n-3):
            fig.text(.5,.15-j*0.05,lineList[j+7], color=color_figure[j+3], fontproperties=font_prop)

    fig.text(.45,.035,"page " + str(page_number), color='black', fontproperties=font_prop)

    
    fig.savefig('data.pdf')
    #plt.show()
    plt.close()

    paths = [path_report_pdf,'data.pdf']
    merge_pdfs(paths, output=path_report_pdf)
    os.remove('data.pdf')
