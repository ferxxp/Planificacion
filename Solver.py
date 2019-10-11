
from MAPS import Map
from Node import Node
from MapDisplay import *
import time

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
    goalParentId = -1
    charMap = Map.getCharMap()
    done = False
    goalParentId = -1
    #Start display dependencies
    [app,Fprint,label]=StartDisplayMap(charMap)
    #start the algorithm
    starttime= time.time()

    while not nodes:
        print("--------------------- number of nodes: "+str(len(nodes)))
        updateDisplay(charMap,app,Fprint,label)
        #para todos los nodos en nodes;si tu distancia a la meta es minima te expandes;el nodo mas cercano se expande;distancia sqrt((x-xi)^2 + ...)

        #[x_goal, y_goal] = Map.getGoal() /// [por definir] Nos da los datos posicion de la meta

        min_dist= 100000 #Valor grande, y que sabemos que no habra distancia en nuestros mapas mayor
        for node in nodes:
            posible_min= sqrt(((node.x-x_goal)^2)+((node.y-y_goal)^2))
            if (posible_min< min_dist)
                min_dist=posible_min
                node_candidato = node

        #Node es ahora el candidato y lo expandimos en todas direcciones
        node = node_candidato


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

