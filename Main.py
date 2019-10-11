from Mapread import *
from Outinfo import *
MApdirectory= Maplist(filedirector)
for CurrentMapDir in MApdirectory:
    print(CurrentMapDir)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,solution,time]=Breathfirst(CurrentMap,InitialNode)
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
