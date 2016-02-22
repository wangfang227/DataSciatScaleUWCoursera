import MapReduce
import sys
import os
import json

"""
Word Count Example in the Simple Python MapReduce Framework
"""
os.getcwd()

mr = MapReduce.MapReduce()

inputfile=os.getcwd()+"/data/books.json"
print inputfile
inputdata = open(inputfile)

inputdata.readlines()
inputdata.readline()

d=[]
for line in inputdata:
    d.append(json.loads(line))
    print json.loads(line)

len(d)
d[0][0]
d[0][1]



# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, 1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
      total += v
    mr.emit((key, total))


test=mr.execute(inputdata, mapper, reducer)
print test

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
