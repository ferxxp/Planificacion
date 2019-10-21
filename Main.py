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
    [Solved,Nodelist,solution,time]=Greedy_Euclideo(CurrentMap,InitialNode,True)
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,solution,time]=Greedy_Manhattan(CurrentMap,InitialNode,True)
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,solution,time]=Dijkstra(CurrentMap,InitialNode,True)
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,solution,time]=AManhattan(CurrentMap,InitialNode,True)
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,solution,time]=AEuclidean(CurrentMap,InitialNode,True)
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    #Works but no output solution
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,solution,time]=BidireccionalM(CurrentMap,InitialNode,True)
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,solution,time]=Random(CurrentMap,InitialNode,True)
    writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
