from Mapread import *
from Outinfo import *
from Solver import *
MApdirectory= Maplist(filedirector)
for CurrentMapDir in MApdirectory:
    print(CurrentMapDir)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    dumpMap(CurrentMap.charMap)
    print(len(CurrentMap.charMap))
    print(len(CurrentMap.charMap[0]))
    [Solved,Nodelist,solution,time]=Bidireccionalclean(CurrentMap,InitialNode)

    # #solve map
    # [Solved,Nodelist,solution,time]=Breathfirst(CurrentMap,InitialNode)
    # #print info
    # writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    # #solve map
    # [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    # [Solved,Nodelist,solution,time]=A_estrella(CurrentMap,InitialNode)
    # writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    # [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    # [Solved,Nodelist,solution,time]=Dijkstra(CurrentMap,InitialNode)
    # writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    # [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    # [Solved,Nodelist,solution,time]=DijkstraA(CurrentMap,InitialNode)
    # writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    # [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    # [Solved,Nodelist,solution,time]=MAnhattan(CurrentMap,InitialNode)
    # writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    #Works but no output solution
    # [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    # [Solved,Nodelist,solution,time]=Bidireccional(CurrentMap,InitialNode)
    # writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
    # [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    # [Solved,Nodelist,solution,time]=Ransom(CurrentMap,InitialNode)
    # writetofile(CurrentMapDir,Solved,time,Nodelist,solution)
