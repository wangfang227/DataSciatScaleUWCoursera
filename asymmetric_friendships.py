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
    key = ' '.join(sorted(list(record)))
    mr.emit_intermediate(key, 1)


def reducer(key, list_of_values):
    total = len(list_of_values)
    pair=key.split()
    if total<2: 
        value1=tuple(sorted(pair))
        value2=tuple(sorted(pair,reverse=True))
        mr.emit(value1)
        mr.emit(value2)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
