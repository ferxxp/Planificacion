
def writetofile(CurrentMapDir,Solved,time,Nodelist,solution):
    f=open("out.txt","a")
    f.write('\n')
    f.write(CurrentMapDir+',')
    f.write(str(Solved)+',')
    f.write(str(time)+',')
    f.write(str(len(Nodelist))+',')
    f.write(str(len(solution))+',')
    for node in solution:
        f.write(str(node.printid())+',')
    f.close()