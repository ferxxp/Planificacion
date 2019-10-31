from Mapread import *
from Outinfo import *
from Solver import *
MApdirectory= Maplist(filedirector)
while True:
    a=0
    for map in MApdirectory:
        print(str(a)+".-"+map.split('/')[len(map.split('/'))-1])
        a=a+1
    validinput=True
    while validinput:
        try:
            modem=int(input('Select Map number:'))
            if modem<len(MApdirectory):
                validinput=False
            else:
                print("mapa no valido")
        except ValueError:
            print("Input no valido")
    print("0.-Breathfirst\n1.-Greedy_Euclideo\n2.-Greedy_Manhattan\n3.-Random\n4.-Dijkstra\n5.-AEuclidean\n6.-AManhattan\n7.-BidireccionalM\n8.-BidireccionalE\n9.-Explorer\n10.-Mostrar Mapa")
    validinput=True
    while validinput:
        try:
            modes=int(input('Select Solver type:'))
            if modes<11:
                validinput=False
            else:
                print("Solver no valido")
        except ValueError:
            print("Input no valido")
    print(str(modem)+" "+str(modes))
    MApname=MApdirectory[modem].split('/')[len(MApdirectory[modem].split('/'))-1]
    if modes==0:
        [CurrentMap,InitialNode]=GetMAP(MApdirectory[modem])
        #solve map
        [Solved,Nodelist,NNodesVisited,solution,time]=Breathfirst(MApname,CurrentMap,InitialNode,True)
        #print info
        writetofile(MApname,"Breathfirst",Solved,time,Nodelist,NNodesVisited,solution)
    elif modes==1:
        [CurrentMap,InitialNode]=GetMAP(MApdirectory[modem])
        #solve map
        [Solved,Nodelist,NNodesVisited,solution,time]=Greedy_Euclideo(MApname,CurrentMap,InitialNode,True)
        #print info
        writetofile(MApname,"Greedy_Euclideo",Solved,time,Nodelist,NNodesVisited,solution)
    elif modes==2:
        [CurrentMap,InitialNode]=GetMAP(MApdirectory[modem])
        #solve map
        [Solved,Nodelist,NNodesVisited,solution,time]=Greedy_Manhattan(MApname,CurrentMap,InitialNode,True)
        #print info
        writetofile(MApname,"Greedy_Manhattan",Solved,time,Nodelist,NNodesVisited,solution)
    elif modes==3:
        [CurrentMap,InitialNode]=GetMAP(MApdirectory[modem])
        #solve map
        [Solved,Nodelist,NNodesVisited,solution,time]=Random(MApname,CurrentMap,InitialNode,True)
        #print info
        writetofile(MApname,"Random",Solved,time,Nodelist,NNodesVisited,solution)
    elif modes==4:
        [CurrentMap,InitialNode]=GetMAP(MApdirectory[modem])
        #solve map
        [Solved,Nodelist,NNodesVisited,solution,time]=Dijkstra(MApname,CurrentMap,InitialNode,True)
        #print info
        writetofile(MApname,"Dijkstra",Solved,time,Nodelist,NNodesVisited,solution)
    elif modes==5:
        [CurrentMap,InitialNode]=GetMAP(MApdirectory[modem])
        #solve map
        [Solved,Nodelist,NNodesVisited,solution,time]=AEuclidean(MApname,CurrentMap,InitialNode,True)
        #print info
        writetofile(MApname,"AEuclidean",Solved,time,Nodelist,NNodesVisited,solution)
    elif modes==6:
        [CurrentMap,InitialNode]=GetMAP(MApdirectory[modem])
        #solve map
        [Solved,Nodelist,NNodesVisited,solution,time]=AManhattan(MApname,CurrentMap,InitialNode,True)
        #print info
        writetofile(MApname,"AManhattan",Solved,time,Nodelist,NNodesVisited,solution)
    elif modes==7:
        [CurrentMap,InitialNode]=GetMAP(MApdirectory[modem])
        #solve map
        [Solved,Nodelist,NNodesVisited,solution,time]=BidireccionalM(MApname,CurrentMap,InitialNode,True)
        #print info
        writetofile(MApname,"BidireccionalM",Solved,time,Nodelist,NNodesVisited,solution)
    elif modes==8:
        [CurrentMap,InitialNode]=GetMAP(MApdirectory[modem])
        #solve map
        [Solved,Nodelist,NNodesVisited,solution,time]=BidireccionalE(MApname,CurrentMap,InitialNode,True)
        #print info
        writetofile(MApname,"BidireccionalE",Solved,time,Nodelist,NNodesVisited,solution)
    elif modes==9:
        print("In idea ocean")
        [CurrentMap,InitialNode]=GetMAP(MApdirectory[modem])
        #solve map
        [Solved,Nodelist,NNodesVisited,solution,time]=Explorer(MApname,CurrentMap,InitialNode,True)
        #print info
        writetofile(MApname,"Explorer",Solved,time,Nodelist,NNodesVisited,solution)
    elif modes==10:
        [CurrentMap,InitialNode]=GetMAP(MApdirectory[modem])
        Onlydisplay(MApname,CurrentMap,InitialNode,True)
