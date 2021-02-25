print("Just trying 2")

filepath = 'a_example'

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print(line)
       cnt += 1
       words = line.split()
       print(words)
       line = fp.readline()