class Point:
    data_names = {
        'barra':(-13.005425, -38.527549),
        'ondina':(-13.005342, -38.509181)
    }
    def __init__(self, lat=None, long=None):
        self.lat = lat
        self.long = long
    def setNameQrf(self, nameQrf):
        coord = self.data_names[nameQrf]
        self.lat = coord[0]
        self.long = coord[1]
        return self


class Servidor:
    def __init__(self, name, mat, hour):
        self.name = name
        self.mat = mat
        self.qrf = None
        self.hour = hour
    def setQRF(self, coord):
        if type(coord) == tuple:
            self.qrf = Point(coord[0], coord[1])
        elif type(coord) == str:
                self.qrf = Point().setNameQrf(coord)
    def getName(self):
        return self.name
    def getQrf(self):
        return self.qrf
