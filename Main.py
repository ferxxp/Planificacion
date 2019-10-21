from Mapread import *
from Outinfo import *
from Solver import *
MApdirectory= Maplist(filedirector)
for CurrentMapDir in MApdirectory:
    print(CurrentMapDir)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    #solve map
    [Solved,Nodelist,solution,time]=Breathfirst(CurrentMap,InitialNode,True)
    #print info
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    #solve map
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,solution,time]=A_estrella(CurrentMap,InitialNode,True)
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,solution,time]=Dijkstra(CurrentMap,InitialNode,True)
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,solution,time]=DijkstraA(CurrentMap,InitialNode,True)
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,solution,time]=MAnhattan(CurrentMap,InitialNode,True)
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    #Works but no output solution
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,solution,time]=Bidireccional(CurrentMap,InitialNode,True)
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,solution,time]=Ransom(CurrentMap,InitialNode,True)
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
