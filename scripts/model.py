class Point:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long


class Servidor:
    def __init__(self, name, mat):
        self.name = name
        self.mat = mat
        self.qrf = None
    def setQRF(self, coord):
        self.qrf = Point(coord[0], coord[1])
    def getName(self):
        return self.name
    def getQrf(self):
        return self.qrf
