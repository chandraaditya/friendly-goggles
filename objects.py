import queue


class Road:
    def __init__(self, name, cost):
        self.fromIntersection = None
        self.toIntersection = None
        self.name = name
        self.cost = cost
        self.carQueue = queue.Queue()

    def addFromAndToIntersection(self, fromIntersection, toIntersection):
        self.fromIntersection = fromIntersection
        self.toIntersection = toIntersection

    def addCar(self, car):
        self.carQueue.put(car)

    def removeCar(self):
        return self.carQueue.get()


class Intersection:
    def __init__(self, iid):
        self.ID = iid
        self.inRoads = dict()
        self.outRoads = dict()

    def addInRoad(self, inRoad):
        if inRoad.name not in self.inRoads:
            self.inRoads[inRoad.name] = inRoad

    def addOutRoad(self, outRoad):
        if outRoad.name not in self.outRoads:
            self.outRoads[outRoad.name] = outRoad


class TrafficLight:
    def __init__(self, intersection):
        self.intersection = intersection
        self.roads = []
        self.time = []
        self.currentRoad = 0
        self.currentTimeOnRoad = 0

    def addTrafficInstruction(self, road, time):
        self.roads.append(road)
        self.time.append(time)

    def updateRoad(self):
        self.currentTimeOnRoad = self.currentTimeOnRoad + 1
        if self.currentTimeOnRoad >= self.time[self.currentRoad] and self.currentRoad < len(self.roads):
            self.currentRoad = self.currentRoad + 1
            self.currentTimeOnRoad = 0
        elif self.currentRoad == len(self.roads):
            self.currentRoad = 0
            self.currentTimeOnRoad = 0


class Car:
    counter = 0

    def __init__(self, path):
        Car.counter += 1
        self.counter = Car.counter
        self.path = path
        self.currentCost = 0
