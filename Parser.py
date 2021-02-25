from random import randint

from objects import Road, Intersection, Car, TrafficLight
import queue

class InitialParser:
    def __init__(self):
        self.filepath = 'c.txt'
        self.CarList = []
        self.RoadList = dict()
        self.IntersectionList = dict()
        self.time = 0

    def inputFileParse(self):
        with open(self.filepath) as fp:
           line = fp.readline()
           words = line.split()
           self.time = int(words[0])
           numIntersection = int(words[1])
           numStreet = int(words[2])
           numCars = int(words[3])
           score = int(words[4])
           cnt = 1
           line = fp.readline()
           cnt = 2
           for x in range(numStreet):
               words = line.split()
               temp = Road(words[2],int(words[3]))
               if words[0] not in self.IntersectionList.keys():
                   self.IntersectionList[words[0]] = Intersection(words[0])
               self.IntersectionList[words[0]].addOutRoad(temp)

               if words[1] not in self.IntersectionList.keys():
                   self.IntersectionList[words[1]] = Intersection(words[1])
               self.IntersectionList[words[1]].addInRoad(temp)

               temp.addFromAndToIntersection(self.IntersectionList[words[0]], self.IntersectionList[words[1]])
               self.RoadList[words[2]] = temp
               #
               line = fp.readline()
               cnt = cnt + 1

           for x in range(numCars):
               words = line.split()
               num = int(words[0])
               temp2 = []
               for j in range(num):
                   temp2.append(self.RoadList[words[j+1]])
               Car(temp2)
               line = fp.readline()

def writer(tfmap):
    filepath = "output.txt"
    with open(filepath , 'w') as fp:
        fp.writelines(str(len(tfmap.values()) )+ "\n")
        for key, i in tfmap.items():
            fp.writelines(i.intersection.ID + "\n")
            fp.writelines(str (len(i.roads) ) + "\n")
            for j in range(len(i.roads)):
                fp.writelines(str(i.roads[j].name) + " "+ str(i.time[j]) + "\n")

def randomiser(interList, time):
    tf = dict()
    for key, x in interList.items():
        timeT = time
        temp = TrafficLight(x)
        for key2, y in x.inRoads.items():
            t = randint(0,timeT)
            timeT = timeT - t
            temp.addTrafficInstruction(y, t)
        tf[x.ID] = temp
    return tf

prad = InitialParser()
prad.inputFileParse()
key = randomiser(prad.IntersectionList, prad.time)
writer(key)