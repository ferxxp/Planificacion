import os
import Node
from MAPS import Map

filedirector = "/Users/fernandoquevedovallejo/Desktop/Planificacion/master-ipr"
files = []

def Maplist(path):
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for directori in d:
            if 'map' in directori:
                files.append(os.path.join(r, directori))
def GetMAP(path):
    print(path)
    charMap = []
    START_X = -1
    END_X = -1
    START_Y = -1
    END_Y = -1
    for r, d, f in os.walk(path):
        for file in f:
            if 'map' in file:
                if '.csv' in file:
                    with open(os.path.join(r,file)) as fileopen:
                        line = fileopen.readline()
                        while line:
                            charLine = line.strip().split(',')
                            charMap.append(charLine)
                            line = fileopen.readline()
                        #print(charMap)
            elif 'README.md' in file:
                with open(os.path.join(r,file)) as fileopen:
                    line =fileopen.readline()
                    while line:
                        if 'Origin'in line:
                            subline = line.split(' ')
                            for pline in subline:
                                if 'Line' in pline:
                                    START_X= int(subline[subline.index(pline)+1].strip(',. '))
                                elif 'Column' in pline:
                                    START_Y= int(subline[subline.index(pline)+1].strip(',. '))

                        elif 'Destiny' in line:
                            subline = line.split(' ')
                            for pline in subline:
                                if 'Line' in pline:
                                    END_X= int(subline[subline.index(pline)+1].strip(',. '))
                                elif 'Column' in pline:
                                    END_Y= int(subline[subline.index(pline)+1].strip(',. '))
                        line =fileopen.readline()
                A = Map(START_X,START_Y,END_X,END_Y,path,charMap)

def CreateAllMaps():
    Maplist(filedirector)
    for maps in files:
        GetMAP(maps)
def CreateMAPnumber(number):
    Maplist(filedirector)
    for maps in files:
        if os.path.join(filedirector,'map'+str(number)) == maps:
            GetMAP(maps)
CreateAllMaps()
CreateMAPnumber(1)