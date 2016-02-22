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
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

#mapper(d[0])

#only show records in line items
def reducer(key, list_of_values):
    # key: order id
    # value: order, and line items
    order=list_of_values[0]
    items=list_of_values[1:]
    for v in items:
      mr.emit((order+v))

#one order has many different line items, the unique order needs to combine
#with different line items one by one, instead of order+all the items (mroe than 27)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
