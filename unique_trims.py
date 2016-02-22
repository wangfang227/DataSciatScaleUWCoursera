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
    key=record[0]
    value=record[1][:-10]
    mr.emit_intermediate(value, 0)


def reducer(key, list_of_values):
    mr.emit(key)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
