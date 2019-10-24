
def writetofile(CurrentMapDir,Solver,Solved,time,Nodelist,NNodesVisited,solution):
    f=open("info_out_nv.txt","a")
    f.write('\n')
    f.write(CurrentMapDir+'\t,')
    f.write(Solver+',')
    f.write(str(Solved)+',')
    f.write(str(time)+',')
    f.write(str(len(Nodelist))+',')
    f.write(str(NNodesVisited)+',')
    f.write(str(len(solution))+',')
    for node in solution:
        f.write(str(node.printid())+',')
    f.close()
