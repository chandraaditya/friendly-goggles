from objects import Road, Intersection,Car
import queue
filepath = 'Files/a.txt'
CarList = []
RoadList = dict()
IntersectionList = dict()

with open(filepath) as fp:
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
       if words[0] not in IntersectionList.keys():
           IntersectionList[words[0]] = Intersection(words[0])
       IntersectionList[words[0]].addOutRoad(temp)

       if words[1] not in IntersectionList.keys():
           IntersectionList[words[1]] = Intersection(words[1])
       IntersectionList[words[1]].addInRoad(temp)

       temp.addFromAndToIntersection(IntersectionList[words[0]], IntersectionList[words[1]])
       RoadList[words[2]] = temp
       #
       line = fp.readline()
       cnt = cnt + 1

   for x in range(numCars):
       words = line.split()
       num = int(words[0])
       temp2 = queue.Queue()
       for j in range(num):
           temp2.put(RoadList[words[j+1]])
       Car(temp2)
       line = fp.readline()