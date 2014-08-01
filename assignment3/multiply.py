import MapReduce
import sys

mr = MapReduce.MapReduce()

N = 5

def mapper(record):
    # key: document identifier
    # value: document contents
    matrix = record[0]
    i = record[1]
    j = record[2]

    if (matrix == 'a'):
      for k in range(0, N):
        mr.emit_intermediate((i, k), record)
    elif (matrix == 'b'):
      for k in range(0, N):
        mr.emit_intermediate((k, j), record)

def reducer(key, list_of_values):
    As = [value for value in list_of_values if (value[0] == 'a')]
    Bs = [value for value in list_of_values if (value[0] == 'b')]

    mr.emit((key[0], key[1], sum([a[3] * b[3] for a in As for b in Bs if a[2] == b[1]])))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
