
import helper


input_file = 'inputs/day10'

def score_trailhead(map, row, col, cur_height):
  if row < 0 or row >= len(map) or col < 0 or col >= len(map[row]):
    return []
  if map[row][col] == 9 and cur_height == 9:
    return [(row, col)]
  if map[row][col] != cur_height:
    return []
  return score_trailhead(map, row+1, col, cur_height+1) + \
         score_trailhead(map, row-1, col, cur_height+1) + \
         score_trailhead(map, row, col+1, cur_height+1) + \
         score_trailhead(map, row, col-1, cur_height+1)

def part_1():
  lines = helper.read_file_as_list_of_strings(input_file)
  map = [[int(c) for c in line] for line in lines]
  total_score = 0
  for row in range(len(map)):
    for col in range(len(map[row])):
      if map[row][col] == 0:
        #print('testing row', row, 'col', col)
        total_score += len(score_trailhead(map, row, col, 0))

  print(total_score)

def part_2():
  pass

part_1()