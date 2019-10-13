class Map:
    def __init__(self, Sx, Sy, Ex, Ey ,Mid,  charMap):
        self.Sx = Sx
        self.Sy = Sy
        self.Ex = Ex
        self.Ey = Ey
        self.Mid = Mid
        self.charMap=charMap

        self.charMap[Sx][Sy]='3'
        self.charMap[Ex][Ey]='4'
    def dump(self):
        print("---------- x "+str(self.Mid))
    def getCharMap(self):
        return self.charMap
    def getXgoal(self):
        return self.Ex
    def getYgoal(self):
        return self.Ey
