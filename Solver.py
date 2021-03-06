
from MAPS import Map
from Node import Node
from MapDisplay import *
import time
import math
import random
def Breathfirst(Mapname,Map,NODE,visual):
#set up-------------------------------------------------------------------------
    nodes = [NODE]
    goalParentId = -1
    charMap = Map.getCharMap()
    done = False
    goalParentId = -1
    #Start display dependencies
    if visual:
        [app,Fprint,label]=StartDisplayclean(charMap,Mapname,"Breathfirst")
#start the algorithm------------------------------------------------------------
    starttime= time.time()
    numberiter=0
    for node in nodes:
        numberiter=numberiter+1
        print(" Number of nodes: "+str(len(nodes)))
        charMap[node.x][node.y]='5'
        if visual:
            updateDisplayclean(charMap,app,Fprint)

        # up--------------------------------------------------------------------
        tmpX = node.x - 1
        tmpY = node.y
        if( charMap[tmpX][tmpY] == '4' ):
            print("up: GOALLLL!!!")
            goalParentId = node.myId
            done = True
            break
        elif ( charMap[tmpX][tmpY] == '0' ):
            print("up: mark visited")
            newNode = Node(tmpX, tmpY, len(nodes), node.myId)
            charMap[tmpX][tmpY] = '2'
            nodes.append(newNode)

        # down------------------------------------------------------------------
        tmpX = node.x + 1
        tmpY = node.y
        if( charMap[tmpX][tmpY] == '4' ):
            print("down: GOALLLL!!!")
            goalParentId = node.myId
            done = True
            break
        elif ( charMap[tmpX][tmpY] == '0' ):
            print("down: mark visited")
            newNode = Node(tmpX, tmpY, len(nodes), node.myId)
            charMap[tmpX][tmpY] = '2'
            nodes.append(newNode)

        # right-----------------------------------------------------------------
        tmpX = node.x
        tmpY = node.y + 1
        if( charMap[tmpX][tmpY] == '4' ):
            print("right: GOALLLL!!!")
            goalParentId = node.myId
            done = True
            break
        elif ( charMap[tmpX][tmpY] == '0' ):
            print("right    : mark visited")
            newNode = Node(tmpX, tmpY, len(nodes), node.myId)
            charMap[tmpX][tmpY] = '2'
            nodes.append(newNode)

        # left------------------------------------------------------------------
        tmpX = node.x
        tmpY = node.y - 1
        if( charMap[tmpX][tmpY] == '4' ):
            print("left: GOALLLL!!!")
            goalParentId = node.myId
            done = True
            break
        elif ( charMap[tmpX][tmpY] == '0' ):
            print("left: mark visited")
            newNode = Node(tmpX, tmpY, len(nodes), node.myId)
            charMap[tmpX][tmpY] = '2'
            nodes.append(newNode)
        print("------------------------------------------")
    # Goal reached create solution----------------------------------------------
    stoptime=time.time()
    print("Goal reached")
    ok = False

    Solution=[Node(Map.getXgoal(),Map.getYgoal(),-5,None)]
    while not ok:
        for node in nodes:
            if( node.myId == goalParentId ):
                Solution.append(node)
                goalParentId = node.parentId
                if( goalParentId == -2):
                    ok = True
    if visual:
        addsolutionclean(app,Solution)
    return[done,nodes,numberiter,Solution,-starttime+stoptime]

def Greedy_Euclideo(Mapname,Map,NODE,visual):
    #set up--------------------------------------------------------------------
    nodes = [NODE]
    candidatenodes=[NODE]
    goalParentId = -1
    charMap = Map.getCharMap()
    done = False
    goalParentId = -1
    #Start display dependencies-------------------------------------------------
    if visual:
        [app,Fprint,label]=StartDisplayclean(charMap,Mapname,"Greedy_Euclideo")
    #start the algorithm--------------------------------------------------------
    print(charMap)
    x_goal=Map.getXgoal()
    y_goal=Map.getYgoal()
    numberiter=0
    starttime= time.time()
    while not done:
        numberiter=numberiter+1
        print("--------------------- number of nodes: "+str(len(nodes)))
        print("--------------------- number of nodes: "+str(len(candidatenodes)))
        if visual:
            updateDisplayclean(charMap,app,Fprint)
        min_dist= float("inf") #Valor grande, y que sabemos que no habra distancia en nuestros mapas mayor
        node = None
        node_candidato=None
        #Select node------------------------------------------------------------
        for nodesearch in candidatenodes:
            posible_min= math.sqrt(pow(nodesearch.x-x_goal,2)+pow(nodesearch.y-y_goal,2))
            if (posible_min< min_dist):
                min_dist=posible_min
                node_candidato = nodesearch
        node = node_candidato
        #expansion del nodo-----------------------------------------------------
        if node:
            candidatenodes.remove(node)
            charMap[node.x][node.y]='5'
            # up----------------------------------------------------------------
            tmpX = node.x - 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' ):
                print("up: GOALLLL!!!")
                goalParentId = node.myId
                done
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("up: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append(newNode)

            # down--------------------------------------------------------------
            tmpX = node.x + 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' ):
                print("down: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("down: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append(newNode)

            # right-------------------------------------------------------------
            tmpX = node.x
            tmpY = node.y + 1
            if( charMap[tmpX][tmpY] == '4' ):
                print("right: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("right    : mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append(newNode)
             # left-------------------------------------------------------------
            tmpX = node.x
            tmpY = node.y - 1
            if( charMap[tmpX][tmpY] == '4' ):
                print("left: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("left: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append(newNode)
        else:
            break
        print("------------------------------------------")

    stoptime=time.time()
    # Goal reached create solution----------------------------------------------
    ok = False

    Solution=[Node(Map.getXgoal(),Map.getYgoal(),-5,None)]
    while not ok:
        for node in nodes:
            if( node.myId == goalParentId ):
                Solution.append(node)
                goalParentId = node.parentId
                if( goalParentId == -2):
                    ok = True
    if visual:
        addsolutionclean(app,Solution)
    return[done,nodes,numberiter,Solution,-starttime+stoptime]

def Greedy_Manhattan(Mapname,Map,NODE,visual):
    #set up--------------------------------------------------------------------
    nodes = [NODE]
    candidatenodes=[NODE]
    goalParentId = -1
    charMap = Map.getCharMap()
    done = False
    goalParentId = -1
    #Start display dependencies
    if visual:
        [app,Fprint,label]=StartDisplayclean(charMap,Mapname,"Greedy_Manhattan")
    #start the algorithm--------------------------------------------------------
    print(charMap)
    x_goal=Map.getXgoal()
    y_goal=Map.getYgoal()
    numberiter=0
    starttime= time.time()
    while not done:
        numberiter=numberiter+1

        print("--------------------- number of nodes: "+str(len(nodes)))
        print("--------------------- number of nodes: "+str(len(candidatenodes)))
        if visual:
            updateDisplayclean(charMap,app,Fprint)
        min_dist= float("inf")
        node = None
        node_candidato=None
        #Select node------------------------------------------------------------
        for nodesearch in candidatenodes:
            posible_min= (abs(nodesearch.x-x_goal)+abs(nodesearch.y-y_goal))
            if (posible_min< min_dist):
                min_dist=posible_min
                node_candidato = nodesearch
        node = node_candidato

        #expansion del nodo-----------------------------------------------------
        if node:
            candidatenodes.remove(node)
            charMap[node.x][node.y]='5'
            # up--------------------------------------------
            tmpX = node.x - 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' ):
                print("up: GOALLLL!!!")
                goalParentId = node.myId
                done
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("up: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append(newNode)

            # down--------------------------------------------
            tmpX = node.x + 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' ):
                print("down: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("down: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append(newNode)

            # right--------------------------------------------
            tmpX = node.x
            tmpY = node.y + 1
            if( charMap[tmpX][tmpY] == '4' ):
                print("right: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("right    : mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append(newNode)
             # left--------------------------------------------
            tmpX = node.x
            tmpY = node.y - 1
            if( charMap[tmpX][tmpY] == '4' ):
                print("left: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("left: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append(newNode)
        else:
            break
        print("------------------------------------------")

    # Goal reached create solution----------------------------------------------
    stoptime=time.time()
    ok = False

    Solution=[Node(Map.getXgoal(),Map.getYgoal(),-5,None)]
    while not ok:
        for node in nodes:
            if( node.myId == goalParentId ):
                Solution.append(node)
                goalParentId = node.parentId
                if( goalParentId == -2):
                    ok = True
    if visual:
        addsolutionclean(app,Solution)
    return[done,nodes,numberiter,Solution,-starttime+stoptime]

def Dijkstra(Mapname,Map,NODE,visual):
    #set up---------------------------------------------------------------------
    nodes = [NODE]
    candidatenodes = [[NODE,0]]
    goalParentId = -1
    charMap = Map.getCharMap()
    done = False
    goalParentId = -1
    cost=0;
    #Start display dependencies
    if visual:
        [app,Fprint,label]=StartDisplayclean(charMap,Mapname,"Dijkstra")
    #start the algorithm--------------------------------------------------------
    numberiter=0
    starttime= time.time()
    while not done:
        numberiter=numberiter+1
        if visual:
            updateDisplayclean(charMap,app,Fprint)
        cost=float("inf")
        node = None
        candidatenode=None
        #select appropiate node-------------------------------------------------
        for sn,sc in candidatenodes:
            if sc < cost:
                candidatenode=sn
                cost=sc
        #expansion del nodo-----------------------------------------------------
        if candidatenode:
            candidatenodes.remove([candidatenode,cost])
            #exploration
            node = candidatenode
            charMap[node.x][node.y]='5'
            tmpX = node.x - 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' ):
                print("up: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("up: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,cost+1])

            # down-------------------------------------------

            tmpX = node.x + 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' ):
                print("down: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("down: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,cost+1])

            # right-------------------------------------------

            tmpX = node.x
            tmpY = node.y + 1
            if( charMap[tmpX][tmpY] == '4' ):
                print("right: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("right    : mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,cost+1])

            # left-------------------------------------------

            tmpX = node.x
            tmpY = node.y - 1
            if( charMap[tmpX][tmpY] == '4' ):
                print("left: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("left: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,cost+1])
        else:
            break
        print("------------------------------------------")

    # Goal reached create solution----------------------------------------------
    stoptime=time.time()
    print("Goal reached")
    ok = False

    Solution=[Node(Map.getXgoal(),Map.getYgoal(),-5,None)]
    while not ok:
        for node in nodes:
            if( node.myId == goalParentId ):
                Solution.append(node)
                goalParentId = node.parentId
                if( goalParentId == -2):
                    ok = True
    if visual:
        addsolutionclean(app,Solution)
    return[done,nodes,numberiter,Solution,-starttime+stoptime]

def Random(Mapname,Map,NODE,visual):
    #set up---------------------------------------------------------------------
    nodes = [NODE]
    candidatenodes = [[NODE,0]]
    goalParentId = -1
    charMap = Map.getCharMap()
    done = False
    goalParentId = -1
    cost=0;
    #Start display dependencies
    if visual:
        [app,Fprint,label]=StartDisplayclean(charMap,Mapname,"Random")
    #start the algorithm--------------------------------------------------------
    numberiter=0
    starttime= time.time()
    while not done:
        numberiter=numberiter+1
        #select appropiate node
        if visual:
            updateDisplayclean(charMap,app,Fprint)

        if candidatenodes:
            #Select node--------------------------------------------------------
            [candidatenode,ignore]=candidatenodes[random.randint(0,len(candidatenodes)-1)]
            candidatenodes.remove([candidatenode,ignore])
            #expansion del nodo-------------------------------------------------
            node = candidatenode
            charMap[node.x][node.y]='5'
            #up----------------------------------------------

            tmpX = node.x - 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' ):
                print("up: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("up: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,cost+1])

            # down----------------------------------------------

            tmpX = node.x + 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' ):
                print("down: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("down: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,cost+1])

            # right----------------------------------------------

            tmpX = node.x
            tmpY = node.y + 1
            if( charMap[tmpX][tmpY] == '4' ):
                print("right: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("right    : mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,cost+1])

            # left----------------------------------------------

            tmpX = node.x
            tmpY = node.y - 1
            if( charMap[tmpX][tmpY] == '4' ):
                print("left: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("left: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,cost+1])
        else:
            break
        print("------------------------------------------")

    stoptime=time.time()
    # Goal reached create solution----------------------------------------------
    ok = False

    Solution=[Node(Map.getXgoal(),Map.getYgoal(),-5,None)]
    while not ok:
        for node in nodes:
            if( node.myId == goalParentId ):
                Solution.append(node)
                goalParentId = node.parentId
                if( goalParentId == -2):
                    ok = True
    if visual:
        addsolutionclean(app,Solution)
    return[done,nodes,numberiter,Solution,-starttime+stoptime]

def AEuclidean(Mapname,Map,NODE,visual):
    #set up-------------------------------------------------------------------------

    nodes = [NODE]
    candidatenodes = [[NODE,0]]
    goalParentId = -1
    charMap = Map.getCharMap()
    done = False
    goalParentId = -1
    cost=0;
    x_goal=Map.getXgoal()
    y_goal=Map.getYgoal()
    #Start display dependencies
    if visual:
        [app,Fprint,label]=StartDisplayclean(charMap,Mapname,"AEuclidean")
    numberiter=0
    starttime= time.time()
    realcost=0
    #start the algorithm--------------------------------------------------------

    while not done:
        numberiter=numberiter+1
        #select appropiate node
        if visual:
            updateDisplayclean(charMap,app,Fprint)
        cost=float("inf")
        node = None
        candidatenode=None
        #Select node------------------------------------------------------------
        for sn,sc in candidatenodes:
            if (sc+math.sqrt(pow(sn.x-x_goal,2)+pow(sn.y-y_goal,2))) < cost:
                candidatenode=sn
                realcost=sc
                cost=sc+math.sqrt(pow(sn.x-x_goal,2)+pow(sn.y-y_goal,2))
        #expansion del nodo-----------------------------------------------------
        if candidatenode:
            candidatenodes.remove([candidatenode,realcost])
            #up----------------------------------------------
            node = candidatenode
            charMap[node.x][node.y]='5'
            tmpX = node.x - 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' ):
                print("up: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("up: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,realcost+1])

            # down----------------------------------------------

            tmpX = node.x + 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' ):
                print("down: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("down: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,realcost+1])

            # right----------------------------------------------

            tmpX = node.x
            tmpY = node.y + 1
            if( charMap[tmpX][tmpY] == '4' ):
                print("right: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("right    : mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,realcost+1])

            # left----------------------------------------------

            tmpX = node.x
            tmpY = node.y - 1
            if( charMap[tmpX][tmpY] == '4' ):
                print("left: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("left: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,realcost+1])
        else:
            break
        print("------------------------------------------")

    # Goal reached create solution----------------------------------------------
    stoptime=time.time()
    print("Goal reached")
    ok = False

    Solution=[Node(Map.getXgoal(),Map.getYgoal(),-5,None)]
    while not ok:
        for node in nodes:
            if( node.myId == goalParentId ):
                Solution.append(node)
                goalParentId = node.parentId
                if( goalParentId == -2):
                    ok = True

    if visual:
        addsolutionclean(app,Solution)
    return[done,nodes,numberiter,Solution,-starttime+stoptime]

def AManhattan(Mapname,Map,NODE,visual):
    #set up---------------------------------------------------------------------

    nodes = [NODE]
    candidatenodes = [[NODE,0]]
    goalParentId = -1
    charMap = Map.getCharMap()
    done = False
    goalParentId = -1
    cost=0;
    x_goal=Map.getXgoal()
    y_goal=Map.getYgoal()
    #Start display dependencies
    if visual:
        [app,Fprint,label]=StartDisplayclean(charMap,Mapname,"AManhattan")
#start the algorithm------------------------------------------------------------
    numberiter=0
    starttime= time.time()
    realcost=0;
    while not done:
        numberiter=numberiter+1
        #select appropiate node
        if visual:
            updateDisplayclean(charMap,app,Fprint)
        cost=float("inf")
        node = None
        candidatenode=None
        #Select node------------------------------------------------------------
        for sn,sc in candidatenodes:
            if (sc+abs(sn.x-x_goal)+abs(sn.y-y_goal)) < cost:
                candidatenode=sn
                realcost=sc
                cost=sc+abs(sn.x-x_goal)+abs(sn.y-y_goal)
        #expansion del nodo-----------------------------------------------------
        if candidatenode:
            candidatenodes.remove([candidatenode,realcost])
            #exploration
            node = candidatenode
            charMap[node.x][node.y]='5'
            #up----------------------------------------------------------

            tmpX = node.x - 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' ):
                print("up: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("up: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,realcost+1])

            # down----------------------------------------------------------

            tmpX = node.x + 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' ):
                print("down: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("down: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,realcost+1])

            # right----------------------------------------------------------

            tmpX = node.x
            tmpY = node.y + 1
            if( charMap[tmpX][tmpY] == '4' ):
                print("right: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("right    : mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,realcost+1])

            # left----------------------------------------------------------

            tmpX = node.x
            tmpY = node.y - 1
            if( charMap[tmpX][tmpY] == '4' ):
                print("left: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("left: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,realcost+1])
        else:
            break
        print("------------------------------------------")
    # Goal reached create solution----------------------------------------------
    stoptime=time.time()
    print("Goal reached")
    ok = False

    Solution=[Node(Map.getXgoal(),Map.getYgoal(),-5,None)]
    while not ok:
        for node in nodes:
            if( node.myId == goalParentId ):
                Solution.append(node)
                goalParentId = node.parentId
                if( goalParentId == -2):
                    ok = True
    if visual:
        addsolutionclean(app,Solution)
    return[done,nodes,numberiter,Solution,-starttime+stoptime]

def BidireccionalM(Mapname,Map,NODE,visual):
#set up-------------------------------------------------------------------------
    nodes = [NODE]
    candidatenodes = [[NODE,0]]
    goalParentId = -1
    charMap = Map.getCharMap()
    done = False
    goalParentId = -1
    cost=0;

    x_start= Map.getXStart()
    y_start= Map.getYStart()

    x_goal=Map.getXgoal()
    y_goal=Map.getYgoal()
    endNode = Node(x_goal, y_goal, 0, -3)
    nodes.append(endNode)

    candidatenodesEnd = [[endNode,0]]

    #Start display dependencies
    if visual:
        [app,Fprint,label]=StartDisplayclean(charMap,Mapname,"BidireccionalM")
    #start the algorithm
    realcost=0;
    realcostEnd=0
    nodex=0
    nodey=0
    numberiter=0
    starttime= time.time()
#start the algorithm------------------------------------------------------------
    while not done:
        if visual:
            updateDisplayclean(charMap,app,Fprint)
        #select node from start
        cost=float("inf")
        node = None
        candidatenode=None
        #Select node start------------------------------------------------------
        for sn,sc in candidatenodes:
            if (sc+abs(sn.x-x_goal)+abs(sn.y-y_goal)) < cost:
                candidatenode=sn
                realcost=sc
                cost=sc+abs(sn.x-x_goal)+abs(sn.y-y_goal)
        #expansion del nodo salida----------------------------------------------
        if candidatenode:
            numberiter=numberiter+1
            candidatenodes.remove([candidatenode,realcost])
            print("Salida")
            print(str(candidatenode.x)+' '+str(candidatenode.y))
            #up---------------------------------------------
            node = candidatenode
            charMap[node.x][node.y]='5'
            tmpX = node.x - 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' or charMap[tmpX][tmpY] == '@' ): # or charMap[tmpX][tmpY] == 2e
                print("up: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                nodex=tmpX
                nodey=tmpY
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("up: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,realcost+1])

            # down---------------------------------------------

            tmpX = node.x + 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' or charMap[tmpX][tmpY] == '@' ):
                print("down: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                nodex=tmpX
                nodey=tmpY
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("down: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,realcost+1])

            # right---------------------------------------------

            tmpX = node.x
            tmpY = node.y + 1
            if( charMap[tmpX][tmpY] == '4' or charMap[tmpX][tmpY] == '@'):
                print("right: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                nodex=tmpX
                nodey=tmpY
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("right    : mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,realcost+1])

            # left---------------------------------------------

            tmpX = node.x
            tmpY = node.y - 1
            if( charMap[tmpX][tmpY] == '4' or charMap[tmpX][tmpY] == '@'):
                print("left: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                nodex=tmpX
                nodey=tmpY
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("left: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,realcost+1])
        else:
            break
        print("------------------------------------------")




        #select node from end---------------------------------------------------
        costEnd=1000
        node = None
        candidatenodeEnd=None
        for sne,sce in candidatenodesEnd:
            print(str(sne.x)+' '+str(sne.y)+' '+str(sce)+' cost '+str(float(sce+abs(sne.x-x_start)+abs(sne.y-y_start))))
            if (sce+abs(sne.x-x_start)+abs(sne.y-y_start)) < costEnd:
                candidatenodeEnd=sne
                realcostEnd=sce
                costEnd=sce+abs(sne.x-x_start)+abs(sne.y-y_start)
        #expansion del nodo end-------------------------------------------------
        if candidatenodeEnd:
            numberiter=numberiter+1
            candidatenodesEnd.remove([candidatenodeEnd,realcostEnd])
            #input("Press Enter to continue...")
            #up-----------------------------------------------------

            node = candidatenodeEnd
            charMap[node.x][node.y]='5'
            tmpX = node.x - 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '3' or charMap[tmpX][tmpY] == '2'): # or charMap[tmpX][tmpY] == 2
                print("up: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                nodex=tmpX
                nodey=tmpY
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("up: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '@' # 2e
                nodes.append(newNode)
                candidatenodesEnd.append([newNode,realcostEnd+1])

            # down---------------------------------------------
            tmpX = node.x + 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '3'or charMap[tmpX][tmpY] == '2' ):
                print("down: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                nodex=tmpX
                nodey=tmpY
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("down: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '@'
                nodes.append(newNode)
                candidatenodesEnd.append([newNode,realcostEnd+1])

            # right---------------------------------------------
            tmpX = node.x
            tmpY = node.y + 1
            if( charMap[tmpX][tmpY] == '3' or charMap[tmpX][tmpY] == '2'):
                print("right: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                nodex=tmpX
                nodey=tmpY
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("right    : mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '@'
                nodes.append(newNode)
                candidatenodesEnd.append([newNode,realcostEnd+1])

            # left---------------------------------------------
            tmpX = node.x
            tmpY = node.y - 1
            if( charMap[tmpX][tmpY] == '3' or charMap[tmpX][tmpY] == '2'):
                print("left: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                nodex=tmpX
                nodey=tmpY
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("left: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '@'
                nodes.append(newNode)
                candidatenodesEnd.append([newNode,realcostEnd+1])
        else:
            break
        print("------------------------------------------")

    # Goal reached create solution----------------------------------------------
    stoptime=time.time()
    Solution=[]
    if done:
        ok = False
        #if visual:app.destroy()
        while not ok:
            for node in nodes:
                if( node.myId == goalParentId ):
                    Solution.append(node)
                    goalParentId = node.parentId
                    if( goalParentId == -3 or goalParentId == -2):
                        ok = True
        goalParentId = candidatenodeEnd.parentId
        ok = False
        for node in nodes:
            if node.x==nodex and node.y==nodey:
                goalParentId=node.myId
        while not ok:
            for node in nodes:
                if( node.myId == goalParentId ):
                    Solution.insert(0,node)
                    goalParentId = node.parentId
                    if( goalParentId == -3 or goalParentId == -2):
                        ok = True
    if visual:
        addsolutionclean(app,Solution)
    return[done,nodes,numberiter,Solution,-starttime+stoptime]

def BidireccionalE(Mapname,Map,NODE,visual):
#set up-------------------------------------------------------------------------
    nodes = [NODE]
    candidatenodes = [[NODE,0]]
    goalParentId = -1
    charMap = Map.getCharMap()
    done = False
    goalParentId = -1
    cost=0;

    x_start= Map.getXStart()
    y_start= Map.getYStart()

    x_goal=Map.getXgoal()
    y_goal=Map.getYgoal()
    endNode = Node(x_goal, y_goal, 0, -3)
    nodes.append(endNode)

    candidatenodesEnd = [[endNode,0]]

    #Start display dependencies
    if visual:
        [app,Fprint,label]=StartDisplayclean(charMap,Mapname,"BidireccionalE")
    #start the algorithm--------------------------------------------------------
    starttime= time.time()
    realcost=0;
    realcostEnd=0
    nodex=0
    nodey=0
    numberiter=0
    while not done:
        numberiter=numberiter+1
        #select appropiate node
        if visual:
            updateDisplayclean(charMap,app,Fprint)
        #select node from start-------------------------------------------------
        cost=float("inf")
        node = None
        candidatenode=None
        for sn,sc in candidatenodes:
            if (sc+math.sqrt(pow(sn.x-x_goal,2)+pow(sn.y-y_goal,2))) < cost:
                candidatenode=sn
                realcost=sc
                cost=sc+math.sqrt(pow(sn.x-x_goal,2)+pow(sn.y-y_goal,2))
        #expansion del nodo-----------------------------------------------------
        if candidatenode:
            candidatenodes.remove([candidatenode,realcost])
            print("Salida")
            #up----------------------------------------------------
            node = candidatenode
            charMap[node.x][node.y]='5'
            tmpX = node.x - 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' or charMap[tmpX][tmpY] == '@' ):
                print("up: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                nodex=tmpX
                nodey=tmpY
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("up: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,realcost+1])

            # down----------------------------------------------------
            tmpX = node.x + 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' or charMap[tmpX][tmpY] == '@' ):
                print("down: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                nodex=tmpX
                nodey=tmpY
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("down: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,realcost+1])

            # right----------------------------------------------------
            tmpX = node.x
            tmpY = node.y + 1
            if( charMap[tmpX][tmpY] == '4' or charMap[tmpX][tmpY] == '@'):
                print("right: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                nodex=tmpX
                nodey=tmpY
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("right    : mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,realcost+1])

            # left----------------------------------------------------
            tmpX = node.x
            tmpY = node.y - 1
            if( charMap[tmpX][tmpY] == '4' or charMap[tmpX][tmpY] == '@'):
                print("left: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                nodex=tmpX
                nodey=tmpY
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("left: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,realcost+1])
        else:
            break
        print("------------------------------------------")




        #select node from end---------------------------------------------------
        costEnd=float("inf")
        node = None
        candidatenodeEnd=None
        numberiter=numberiter+1
        for sne,sce in candidatenodesEnd:
            if (sce+math.sqrt(pow(sne.x-x_start,2)+pow(sne.y-y_start,2))) < costEnd:
                candidatenodeEnd=sne
                realcostEnd=sce
                costEnd=sce+math.sqrt(pow(sne.x-x_start,2)+pow(sne.y-y_start,2))

        if candidatenodeEnd:
            candidatenodesEnd.remove([candidatenodeEnd,realcostEnd])
            print("meta")
            #up----------------------------------------------------
            node = candidatenodeEnd
            charMap[node.x][node.y]='5'
            tmpX = node.x - 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '3' or charMap[tmpX][tmpY] == '2'): # or charMap[tmpX][tmpY] == 2
                print("up: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                nodex=tmpX
                nodey=tmpY
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("up: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '@' # 2e
                nodes.append(newNode)
                candidatenodesEnd.append([newNode,realcostEnd+1])

            # down----------------------------------------------------
            tmpX = node.x + 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '3'or charMap[tmpX][tmpY] == '2' ):
                print("down: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                nodex=tmpX
                nodey=tmpY
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("down: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '@'
                nodes.append(newNode)
                candidatenodesEnd.append([newNode,realcostEnd+1])

            # right----------------------------------------------------
            tmpX = node.x
            tmpY = node.y + 1
            if( charMap[tmpX][tmpY] == '3' or charMap[tmpX][tmpY] == '2'):
                print("right: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                nodex=tmpX
                nodey=tmpY
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("right    : mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '@'
                nodes.append(newNode)
                candidatenodesEnd.append([newNode,realcostEnd+1])

            # left----------------------------------------------------
            tmpX = node.x
            tmpY = node.y - 1
            if( charMap[tmpX][tmpY] == '3' or charMap[tmpX][tmpY] == '2'):
                print("left: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                nodex=tmpX
                nodey=tmpY
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("left: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '@'
                nodes.append(newNode)
                candidatenodesEnd.append([newNode,realcostEnd+1])
        else:
            break
        print("------------------------------------------")

    # Goal reached create solution----------------------------------------------
    stoptime=time.time()
    Solution=[]
    if done:
        ok = False
        #if visual:app.destroy()
        while not ok:
            for node in nodes:
                if( node.myId == goalParentId ):
                    Solution.append(node)
                    goalParentId = node.parentId
                    if( goalParentId == -3 or goalParentId == -2):
                        ok = True
        goalParentId = candidatenodeEnd.parentId
        ok = False
        for node in nodes:
            if node.x==nodex and node.y==nodey:
                goalParentId=node.myId
        while not ok:
            for node in nodes:
                if( node.myId == goalParentId ):
                    Solution.insert(0,node)
                    goalParentId = node.parentId
                    if( goalParentId == -3 or goalParentId == -2):
                        ok = True
    if visual:
        addsolutionclean(app,Solution)
    return[done,nodes,numberiter,Solution,-starttime+stoptime]

def Explorer(Mapname,Map,NODE,visual):
#set up-------------------------------------------------------------------------
    nodes = [NODE]
    candidatenodes = [[NODE,0]]
    goalParentId = -1
    charMap = Map.getCharMap()
    done = False
    x_goal=Map.getXgoal()
    y_goal=Map.getYgoal()
    goalParentId = -1
    cost=0;
    #Start display dependencies
    if visual:
        [app,Fprint,label]=StartDisplayclean(charMap,Mapname,"Explorer")
#start the algorithm------------------------------------------------------------
    numberiter=0
    starttime= time.time()
    while not done:
        numberiter=numberiter+1
        if visual:
            updateDisplayclean(charMap,app,Fprint)
        cost=float("inf")
        node = None
        candidatenode=None
        #Select node -----------------------------------------------------------
        for sn,sc in candidatenodes:
            if ((sc/(nnewnodes(sn,charMap)))+math.sqrt(pow(sn.x-x_goal,2)+pow(sn.y-y_goal,2))) < cost:
                candidatenode=sn
                realcost=sc
                cost=((sc/(nnewnodes(sn,charMap)))+math.sqrt(pow(sn.x-x_goal,2)+pow(sn.y-y_goal,2)))
            print(nnewnodes(sn,charMap)**2)
            print((sc/(nnewnodes(sn,charMap)))+math.sqrt(pow(sn.x-x_goal,2)+pow(sn.y-y_goal,2)))
        #expansion del nodo ----------------------------------------------------
        if candidatenode:
            candidatenodes.remove([candidatenode,realcost])
            #up-----------------------------------------------------
            node = candidatenode
            charMap[node.x][node.y]='5'
            tmpX = node.x - 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' ):
                print("up: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("up: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,cost+1])

            # down-----------------------------------------------------
            tmpX = node.x + 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' ):
                print("down: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("down: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,cost+1])

            # right-----------------------------------------------------
            tmpX = node.x
            tmpY = node.y + 1
            if( charMap[tmpX][tmpY] == '4' ):
                print("right: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("right    : mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,cost+1])

            # left-----------------------------------------------------
            tmpX = node.x
            tmpY = node.y - 1
            if( charMap[tmpX][tmpY] == '4' ):
                print("left: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("left: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '2'
                nodes.append(newNode)
                candidatenodes.append([newNode,cost+1])
        else:
            break
        print("------------------------------------------")

    stoptime=time.time()
    print("Goal reached")
    ok = False

    Solution=[Node(Map.getXgoal(),Map.getYgoal(),-5,None)]
    while not ok:
        for node in nodes:
            if( node.myId == goalParentId ):
                Solution.append(node)
                goalParentId = node.parentId
                if( goalParentId == -2):
                    ok = True
    if visual:
        addsolutionclean(app,Solution)
    return[done,nodes,numberiter,Solution,-starttime+stoptime]

def Onlydisplay(Mapname,Map,NODE,visual):
    charMap = Map.getCharMap()
    if visual:
        [app,Fprint,label]=StartDisplayclean(charMap,Mapname," ")
        updateDisplayclean(charMap,app,Fprint)

def nnewnodes(node,charMap):
    x=node.x
    y=node.y
    a=0
    if charMap[x+1][y]=='0':
        a=a+1
    if charMap[x+1][y+1]=='0':
            a=a+1
    if charMap[x][y+1]=='0':
            a=a+1
    if charMap[x-1][y+1]=='0':
            a=a+1
    if charMap[x-1][y]=='0':
            a=a+1
    if charMap[x-1][y-1]=='0':
            a=a+1
    if charMap[x][y-1]=='0':
            a=a+1
    if charMap[x+1][y-1]=='0':
            a=a+1
    a/2
    if a<1:
        a=1
    return a
