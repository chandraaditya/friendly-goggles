filepath = 'Files/a.txt'

CarList = []
RoadList = []
IntersectionList = []

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
       print(words)
       line = fp.readline()
       cnt = cnt + 1

   for x in range(numCars):
       words = line.split()
       num = int(words[0])
       Car(num, words[1:num+1])
       line = fp.readline()