class Map:
    def __init__(self, Sx, Sy, Ex, Ey ,Mid,  charMap):
        self.Sx = Sx
        self.Sy = Sy
        self.Ex = Ex
        self.Ey = Ey
        self.Mid = Mid
        self.charMap=charMap
    def dump(self):
        print("---------- x "+str(self.Mid))
