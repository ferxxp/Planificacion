
from MAPS import Map
from Node import Node
from MapDisplay import *


def dumpMap(charMap):
    for line in charMap:
        print(line)

def Breathfirst(Map,NODE):
    nodes = [NODE]
    done = False
    goalParentId = -1
    charMap = Map.getCharMap()
    dumpMap(charMap)
    done = False
    goalParentId = -1

    [app,Fprint,label]=StartDisplayMap(charMap)

    while not done:
        print("--------------------- number of nodes: "+str(len(nodes)))

        for node in nodes:
            #node.dump()
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
            #dumpMap(charMap)
        done=True
    print("%%%%%%%%%%%%%%%%%%%")
    ok = False
    app.destroy()
    while not ok:
        for node in nodes:
            if( node.myId == goalParentId ):
                node.dump()
                goalParentId = node.parentId
                if( goalParentId == -2):
                    print("%%%%%%%%%%%%%%%%%2")
                    ok = True
