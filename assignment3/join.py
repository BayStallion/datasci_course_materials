import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
  orders = [item for item in list_of_values if (item[0] == 'order')]
  line_items = [item for item in list_of_values if (item[0] == 'line_item')]

  for order in orders:
    for line_item in line_items:
      #print order + line_item
      #print len(order + line_item)
      mr.emit(order + line_item)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
