import MapReduce
import sys

mr = MapReduce.MapReduce()

n = 5

def mapper(record):
    key=record[0]
    row=record[1]
    col=record[2]
    value=record[3]
    if key=='a': mr.emit_intermediate(key, [row,col,value])
    if key=='b': mr.emit_intermediate(key, [col,row,value])
        
def reducer(key, list_of_values):
    afull={}
    bfull={}
    m=0
    if key=='a':
        for i in range(n):
            for j in range(n):
                afull[(i,j)]=0
        for v in list_of_values:
            afull[(v[0],v[1])]=v[2]
            
        for i in range(n):
            for j in range(n):
                bfull[(i,j)]=0
        for v in mr.intermediate['b']:
            bfull[(v[0],v[1])]=v[2]
    
        for i in range(n):
            for j in range(n):
                m=0
                for k in range(n):
                    m+=afull[(i,k)]*bfull[(j,k)]
                mr.emit((i,j,m))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)