from Mapread import *
from Outinfo import *
from Solver import *

MApdirectory= Maplist(filedirector)
Vis=False

for CurrentMapDir in MApdirectory:
    print(CurrentMapDir)
    MApname=CurrentMapDir.split('/')[len(CurrentMapDir.split('/'))-1]
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    #solve map
    [Solved,Nodelist,NNodesVisited,solution,time]=Breathfirst(MApname,CurrentMap,InitialNode,Vis)

    #print info
    writetofile(MApname,"Breathfirst",Solved,time,Nodelist,NNodesVisited,solution)
    #solve map
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,NNodesVisited,solution,time]=Greedy_Euclideo(MApname,CurrentMap,InitialNode,Vis)
    writetofile(MApname,"Greedy_Euclideo",Solved,time,Nodelist,NNodesVisited,solution)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,NNodesVisited,solution,time]=Greedy_Manhattan(MApname,CurrentMap,InitialNode,Vis)
    writetofile(MApname,"Greedy_Manhattan",Solved,time,Nodelist,NNodesVisited,solution)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,NNodesVisited,solution,time]=Dijkstra(MApname,CurrentMap,InitialNode,Vis)
    writetofile(MApname,"Dijkstra",Solved,time,Nodelist,NNodesVisited,solution)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,NNodesVisited,solution,time]=AManhattan(MApname,CurrentMap,InitialNode,Vis)
    writetofile(MApname,"AManhattan",Solved,time,Nodelist,NNodesVisited,solution)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,NNodesVisited,solution,time]=AEuclidean(MApname,CurrentMap,InitialNode,Vis)
    writetofile(MApname,"AEuclidean",Solved,time,Nodelist,NNodesVisited,solution)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,NNodesVisited,solution,time]=BidireccionalM(MApname,CurrentMap,InitialNode,Vis)
    writetofile(MApname,"BidireccionalM",Solved,time,Nodelist,NNodesVisited,solution)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,NNodesVisited,solution,time]=BidireccionalE(MApname,CurrentMap,InitialNode,Vis)
    writetofile(MApname,"BidireccionalE",Solved,time,Nodelist,NNodesVisited,solution)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,NNodesVisited,solution,time]=Random(MApname,CurrentMap,InitialNode,Vis)
    writetofile(MApname,"Random",Solved,time,Nodelist,NNodesVisited,solution)
    [CurrentMap,InitialNode]=GetMAP(CurrentMapDir)
    [Solved,Nodelist,NNodesVisited,solution,time]=Explorer(MApname,CurrentMap,InitialNode,Vis)
    writetofile(MApname,"Explorer",Solved,time,Nodelist,NNodesVisited,solution)
