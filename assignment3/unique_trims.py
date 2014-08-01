import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    dna = record[1][0:len(record[1]) - 10]
    mr.emit_intermediate(dna, 1)

def reducer(key, list_of_values):
	mr.emit(key)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
