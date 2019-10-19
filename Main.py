from Mapread import *
from Outinfo import *
from Solver import *
MApdirectory= Maplist(filedirector)
for CurrentMapDir in MApdirectory:
    print(CurrentMapDir)
    
    #Works but no output solution
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,solution,time]=Bidireccional(CurrentMap,InitialNode)
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,solution,time]=Ransom(CurrentMap,InitialNode)
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
