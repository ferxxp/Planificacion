from Mapread import *
from Outinfo import *
from Solver import *
MApdirectory= Maplist(filedirector)
for CurrentMapDir in MApdirectory:
    print(CurrentMapDir)
    #create Map
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    #solve map
    [Solved,Nodelist,solution,time]=Breathfirst(CurrentMap,InitialNode)
    #print info
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    #solve map
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,solution,time]=A_estrella(CurrentMap,InitialNode)
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,solution,time]=Dijkstra(CurrentMap,InitialNode)
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,solution,time]=DijkstraA(CurrentMap,InitialNode)
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,solution,time]=MAnhattan(CurrentMap,InitialNode)
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
