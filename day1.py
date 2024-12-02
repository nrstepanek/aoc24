
from collections import Counter
import helper


input_file = 'inputs/day1'

def part_1():
  lines = helper.read_file_as_list_of_strings(input_file)
  list_1 = []
  list_2 = []
  for line in lines:
    ints = [int(x) for x in line.split()]
    list_1.append(ints[0])
    list_2.append(ints[1])
  list_1.sort()
  list_2.sort()
  total = 0
  for x, y in zip(list_1, list_2):
    total += abs(x - y)
  print(total)

def part_2():
  lines = helper.read_file_as_list_of_strings(input_file)
  list_1 = []
  list_2 = []
  for line in lines:
    ints = [int(x) for x in line.split()]
    list_1.append(ints[0])
    list_2.append(ints[1])
  list_2_counter = Counter(list_2)
  total = 0
  for num in list_1:
    total += num * list_2_counter[num]
  print(total)

part_1()
part_2()