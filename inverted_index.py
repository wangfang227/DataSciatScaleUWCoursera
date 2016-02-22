import MapReduce
import sys
import os
import json
import string

"""
Word Count Example in the Simple Python MapReduce Framework
"""
os.getcwd()

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words: 
      mr.emit_intermediate(w, key)

#mapper(d[0])


def reducer(key, list_of_values):
    # key: word
    # value: list of doc ids
    total=list(set(list_of_values))
    mr.emit((key, total))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
