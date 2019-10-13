from Mapread import *
from Outinfo import *
from Solver import *
MApdirectory= Maplist(filedirector)
for CurrentMapDir in MApdirectory:
    print(CurrentMapDir)
    #create Map
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    #solve map
    #[Solved,Nodelist,solution,time]=Breathfirst(CurrentMap,InitialNode)
    #print info
    #writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    #solve map
    [Solved,Nodelist,solution,time]=A_estrella(CurrentMap,InitialNode)
    #print info
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
