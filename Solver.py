
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
    print(stoptime-starttime)
    return[node,Solution,starttime-stoptime]
