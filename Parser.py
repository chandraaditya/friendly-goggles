from objects import Road, Intersection,Car
import queue

class InitialParser:
    def __init__(self):
        filepath = 'Files/a.txt'
        CarList = []
        RoadList = dict()
        IntersectionList = dict()

    def inputFileParse(self):
        with open(self.filepath) as fp:
           line = fp.readline()
           words = line.split()
           time = int(words[0])
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
    list = tfmap.toList()
    with open(filepath) as fp:
        fp.writelines(len(list))
        for i in range(len(list)):
            fp.writelines(list[i].intersection.id)
            fp.writelines(len(list[i].roads))
            for j in range(len(list[i].roads)):
                fp.writelines(list[i].roads[j].name + str(list[i].time[j]))
