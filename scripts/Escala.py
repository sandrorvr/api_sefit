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
        arr = [self.length(point, wk.getQrf()) for wk in self.listOfWorker]
        return sorted(arr, reverse=False)


if __name__ == '__main__':
    s1 = Servidor('sandro', 1)
    s1.setQRF('ondina')
    s2 = Servidor('sandro', 1)
    s2.setQRF('barra')

    esc = Schedule()
    esc.setWorker(s1)
    esc.setWorker(s2)

    print(esc.rangeWorker(Point(10,10)))