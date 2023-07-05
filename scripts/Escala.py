import math
from model import Servidor, Point

class Schedule:
    def __init__(self):
        self.listOfWorker = []
    
    def setWorker(self, wk):
        self.listOfWorker.append(wk)
    
    def length(self, p1, p2):
        x2 = math.pow(p1.long - p2.long, 2)
        y2 = math.pow(p1.lat - p2.lat, 2)
        return math.sqrt(x2+y2)
    
    def rangeWorker(self, point):
        return [ self.length(point, p) for p in self.listOfWorker]


if __name__ == '__main__':
    s1 = Servidor('sandro', 1).setQRF((3,3))
    s2 = Servidor('sandro', 1).setQRF((10,10))
    s3 = Servidor('sandro', 1).setQRF((15,15))

    esc = Schedule()
    esc.setWorker(s1)
    esc.setWorker(s2)
    esc.setWorker(s3)

    print(esc.rangeWorker(Point(2,2)))