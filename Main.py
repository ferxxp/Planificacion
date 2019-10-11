from Mapread import *

MApdirectory= Maplist(filedirector)
for CurrentMapDir in MApdirectory:
    print(CurrentMapDir)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Nodelist,solution,time]=Breathfirst(CurrentMap,InitialNode)
    f=open("out.txt","a")
    f.write(str(time)+',')
    f.write(str(len(Nodelist))+',')
    f.write(str(len(solution))+',')
    for node in solution:
        f.write(str(node.printid())+',')
    f.write('\n')
