from Mapread import *
from Outinfo import *
from Solver import *
MApdirectory= Maplist(filedirector)
for CurrentMapDir in MApdirectory:

    #Works but no output solution
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,solution,time]=Ransom(CurrentMap,InitialNode)
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
