
from MAPS import Map
from Node import Node
from MapDisplay import *
import time
import math
import random
def Breathfirst(Map,NODE):
    #set up
    nodes = [NODE]
    goalParentId = -1
    charMap = Map.getCharMap()
    done = False
    goalParentId = -1
    #Start display dependencies
    [app,Fprint,label]=StartDisplayMap(charMap)
    #start the algorithm
    starttime= time.time()
    for node in nodes:
        print(" Number of nodes: "+str(len(nodes)))
        updateDisplay(charMap,app,Fprint,label)

        # up
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

        # down
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

        # right
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

        # left
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

    stoptime=time.time()
    print("Goal reached")
    ok = False
    app.destroy()
    Solution=[]
    while not ok:
        for node in nodes:
            if( node.myId == goalParentId ):
                Solution.append(node)
                goalParentId = node.parentId
                if( goalParentId == -2):
                    ok = True
    return[done,nodes,Solution,-starttime+stoptime]

def A_estrella(Map,NODE):
    #set up
    nodes = [NODE]
    candidatenodes=[NODE]
    goalParentId = -1
    charMap = Map.getCharMap()
    done = False
    goalParentId = -1
    #Start display dependencies
    [app,Fprint,label]=StartDisplayMap(charMap)
    #start the algorithm
    starttime= time.time()
    print(charMap)
    x_goal=Map.getXgoal()
    y_goal=Map.getYgoal()

    while not done:

        print("--------------------- number of nodes: "+str(len(nodes)))
        print("--------------------- number of nodes: "+str(len(candidatenodes)))
        updateDisplay(charMap,app,Fprint,label)
        #para todos los nodos en nodes;si tu distancia a la meta es minima te expandes;el nodo mas cercano se expande;distancia sqrt((x-xi)^2 + ...)
        #[x_goal, y_goal] = Map.getGoal() /// [por definir] Nos da los datos posicion de la meta
        min_dist= 100000 #Valor grande, y que sabemos que no habra distancia en nuestros mapas mayor
        node = None
        node_candidato=None
        for nodesearch in candidatenodes:
            posible_min= math.sqrt(pow(nodesearch.x-x_goal,2)+pow(nodesearch.y-y_goal,2))
            if (posible_min< min_dist):
                min_dist=posible_min
                node_candidato = nodesearch
        #Node es ahora el candidato y lo expandimos en todas direcciones
        node = node_candidato

        #can not explore same node again
        if node:
            candidatenodes.remove(node)
            # up
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

            # down
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

            # right
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
             # left
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
    print("Goal reached")
    ok = False
    app.destroy()
    Solution=[]
    while not ok:
        for node in nodes:
            if( node.myId == goalParentId ):
                Solution.append(node)
                goalParentId = node.parentId
                if( goalParentId == -2):
                    ok = True
    return[done,nodes,Solution,-starttime+stoptime]

def Dijkstra(Map,NODE):
    #set up
    nodes = [NODE]
    candidatenodes = [[NODE,0]]
    goalParentId = -1
    charMap = Map.getCharMap()
    done = False
    goalParentId = -1
    cost=0;
    #Start display dependencies
    [app,Fprint,label]=StartDisplayMap(charMap)
    #start the algorithm
    starttime= time.time()
    while not done:
        #select appropiate node
        updateDisplay(charMap,app,Fprint,label)
        cost=1000
        node = None
        candidatenode=None
        for sn,sc in candidatenodes:
            if sc < cost:
                candidatenode=sn
                cost=sc
        if candidatenode:
            candidatenodes.remove([candidatenode,cost])
            #exploration
            node = candidatenode
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

            # down
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

            # right
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

            # left
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
    app.destroy()
    Solution=[]
    while not ok:
        for node in nodes:
            if( node.myId == goalParentId ):
                Solution.append(node)
                goalParentId = node.parentId
                if( goalParentId == -2):
                    ok = True
    return[done,nodes,Solution,-starttime+stoptime]

def Ransom(Map,NODE):
    #set up
    nodes = [NODE]
    candidatenodes = [[NODE,0]]
    goalParentId = -1
    charMap = Map.getCharMap()
    done = False
    goalParentId = -1
    cost=0;
    #Start display dependencies
    [app,Fprint,label]=StartDisplayMap(charMap)
    #start the algorithm
    starttime= time.time()
    while not done:
        #select appropiate node
        updateDisplay(charMap,app,Fprint,label)

        if candidatenodes:
            print(random.randint(0,len(candidatenodes)))
            [candidatenode,ignore]=candidatenodes[random.randint(0,len(candidatenodes)-1)]
            candidatenodes.remove([candidatenode,ignore])
            #exploration
            node = candidatenode
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

            # down
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

            # right
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

            # left
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
    app.destroy()
    Solution=[]
    while not ok:
        for node in nodes:
            if( node.myId == goalParentId ):
                Solution.append(node)
                goalParentId = node.parentId
                if( goalParentId == -2):
                    ok = True
    return[done,nodes,Solution,-starttime+stoptime]

def DijkstraA(Map,NODE):
    #set up
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
    [app,Fprint,label]=StartDisplayMap(charMap)
    #start the algorithm
    starttime= time.time()
    realcost=0
    while not done:
        #select appropiate node
        updateDisplay(charMap,app,Fprint,label)
        cost=1000
        node = None
        candidatenode=None
        for sn,sc in candidatenodes:
            if (sc+math.sqrt(pow(sn.x-x_goal,2)+pow(sn.y-y_goal,2))) < cost:
                candidatenode=sn
                realcost=sc
                cost=sc+math.sqrt(pow(sn.x-x_goal,2)+pow(sn.y-y_goal,2))
        if candidatenode:
            candidatenodes.remove([candidatenode,realcost])
            #exploration
            node = candidatenode
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

            # down
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

            # right
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

            # left
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

    stoptime=time.time()
    print("Goal reached")
    ok = False
    app.destroy()
    Solution=[]
    while not ok:
        for node in nodes:
            if( node.myId == goalParentId ):
                Solution.append(node)
                goalParentId = node.parentId
                if( goalParentId == -2):
                    ok = True
    return[done,nodes,Solution,-starttime+stoptime]

def MAnhattan(Map,NODE):
    #set up
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
    [app,Fprint,label]=StartDisplayMap(charMap)
    #start the algorithm
    starttime= time.time()
    realcost=0;
    while not done:
        #select appropiate node
        updateDisplay(charMap,app,Fprint,label)
        cost=1000
        node = None
        candidatenode=None
        for sn,sc in candidatenodes:
            if (sc+abs(sn.x-x_goal)+abs(sn.y-y_goal)) < cost:
                candidatenode=sn
                realcost=sc
                cost=sc+abs(sn.x-x_goal)+abs(sn.y-y_goal)
        if candidatenode:
            candidatenodes.remove([candidatenode,realcost])
            #exploration
            node = candidatenode
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

            # down
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

            # right
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

            # left
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

    stoptime=time.time()
    print("Goal reached")
    ok = False
    app.destroy()
    Solution=[]
    while not ok:
        for node in nodes:
            if( node.myId == goalParentId ):
                Solution.append(node)
                goalParentId = node.parentId
                if( goalParentId == -2):
                    ok = True
    return[done,nodes,Solution,-starttime+stoptime]

def Bidireccional(Map,NODE):
    #set up
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
    [app,Fprint,label]=StartDisplayMap(charMap)
    #start the algorithm
    starttime= time.time()
    realcost=0;
    realcostEnd=0
    while not done:
        #select appropiate node
        updateDisplay(charMap,app,Fprint,label)
        #select node from start
        cost=1000
        node = None
        candidatenode=None
        for sn,sc in candidatenodes:
            if (sc+abs(sn.x-x_goal)+abs(sn.y-y_goal)) < cost:
                candidatenode=sn
                realcost=sc
                cost=sc+abs(sn.x-x_goal)+abs(sn.y-y_goal)
        if candidatenode:
            candidatenodes.remove([candidatenode,realcost])

            print("Salida")


            #exploration
            node = candidatenode
            tmpX = node.x - 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' or charMap[tmpX][tmpY] == '@' ): # or charMap[tmpX][tmpY] == 2e
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

            # down
            tmpX = node.x + 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '4' or charMap[tmpX][tmpY] == '@' ):
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

            # right
            tmpX = node.x
            tmpY = node.y + 1
            if( charMap[tmpX][tmpY] == '4' or charMap[tmpX][tmpY] == '@'):
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

            # left
            tmpX = node.x
            tmpY = node.y - 1
            if( charMap[tmpX][tmpY] == '4' or charMap[tmpX][tmpY] == '@'):
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




        #select node from end
        costEnd=1000
        node = None
        candidatenodeEnd=None
        for sne,sce in candidatenodesEnd:
            if (sce+abs(sne.x-x_start)+abs(sne.y-y_start)) < costEnd:
                candidatenodeEnd=sne
                realcostEnd=sce
                costEnd=sce+abs(sne.x-x_start)+abs(sne.y-y_start)

        if candidatenodeEnd:
            candidatenodesEnd.remove([candidatenodeEnd,realcostEnd])
            print("meta")
            #exploration
            node = candidatenodeEnd
            tmpX = node.x - 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '3' or charMap[tmpX][tmpY] == '2'): # or charMap[tmpX][tmpY] == 2
                print("up: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("up: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '@' # 2e
                nodes.append(newNode)
                candidatenodesEnd.append([newNode,realcost+1])

            # down
            tmpX = node.x + 1
            tmpY = node.y
            if( charMap[tmpX][tmpY] == '3'or charMap[tmpX][tmpY] == '2' ):
                print("down: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("down: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '@'
                nodes.append(newNode)
                candidatenodesEnd.append([newNode,realcost+1])

            # right
            tmpX = node.x
            tmpY = node.y + 1
            if( charMap[tmpX][tmpY] == '3' or charMap[tmpX][tmpY] == '2'):
                print("right: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("right    : mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '@'
                nodes.append(newNode)
                candidatenodesEnd.append([newNode,realcost+1])

            # left
            tmpX = node.x
            tmpY = node.y - 1
            if( charMap[tmpX][tmpY] == '3' or charMap[tmpX][tmpY] == '2'):
                print("left: GOALLLL!!!")
                goalParentId = node.myId
                done = True
                break
            elif ( charMap[tmpX][tmpY] == '0' ):
                print("left: mark visited")
                newNode = Node(tmpX, tmpY, len(nodes), node.myId)
                charMap[tmpX][tmpY] = '@'
                nodes.append(newNode)
                candidatenodesEnd.append([newNode,realcost+1])
        else:
            break
        print("------------------------------------------")


    stoptime=time.time()
    Solution=[]
    if done:
        goalParentId = candidatenode.parentId
        ok = False
        #app.destroy()

        while not ok:
            for node in nodes:
                if( node.myId == goalParentId ):
                    Solution.append(node)
                    goalParentId = node.parentId
                    if( goalParentId == -2):
                        ok = True
        goalParentId = candidatenodeEnd.parentId
        ok = False
        while not ok:
            for node in nodes:
                print(goalParentId)
                if( node.myId == goalParentId ):
                    print("stuck")
                    Solution.insert(0,node)
                    goalParentId = node.parentId
                    if( goalParentId == -3):
                        ok = True
        print("stuck out")
    return[done,nodes,Solution,-starttime+stoptime]

def Breathfirstclean(Map,NODE):
    #set up
    nodes = [NODE]
    goalParentId = -1
    charMap = Map.getCharMap()
    done = False
    goalParentId = -1
    #Start display dependencies
    [app,Fprint,label]=StartDisplayclean(charMap)
    #start the algorithm
    starttime= time.time()
    for node in nodes:
        print(" Number of nodes: "+str(len(nodes)))
        updateDisplayclean(charMap,app,Fprint)

        # up
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

        # down
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

        # right
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

        # left
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

    stoptime=time.time()
    print("Goal reached")
    ok = False
    Solution=[]
    while not ok:
        for node in nodes:
            if( node.myId == goalParentId ):
                Solution.append(node)
                goalParentId = node.parentId
                if( goalParentId == -2):
                    ok = True
    addsolutionclean(app,Solution)
    return[done,nodes,Solution,-starttime+stoptime]
