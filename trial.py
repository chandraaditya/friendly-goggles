print("Just trying 2")

filepath = 'Files/a.txt'

with open(filepath) as fp:
   line = fp.readline()
   words = line.split()
   time = int(words[0])
   numIntersection = int(words[1])
   numStreet = int(words[2])
   numCars = int(words[3])
   score = int(words[4])
   cnt = 1
   while line:
       print(line)
       cnt += 1
       words = line.split()
       print(words)
       line = fp.readline()