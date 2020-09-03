import numpy as np 
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

    m[2]="%.12s" % str(0.00000037+t[2]*0.0001)
    p[2]="0 1.002 0.001613"
    v[2]="1 %.6s %.6s" % (str(0),str(1.1))

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

# Create data_info
    f1= open(path_info,"w+")
    f1.write(str(object_number)+"\n")
    f1.write("The first star system Sy1\n")
    for j in range(min(object_number,3)):
        f1.write("m%d= " % (j+1) + m[j] +"  p%d=("% (j+1) +p[j]+ ")  v%d= ("% (j+1)+v[j]+")\n")
    
    f1.write("\n")
    if (object_number>3):
        f1.write("The second star system Sy2\n")
        for j in range(3,object_number):
            f1.write("m%d= " % (j+1) + m[j] +"  p%d=("% (j+1) +p[j]+ ")  v%d= ("% (j+1)+v[j]+")\n")
    
    f1.close() 


