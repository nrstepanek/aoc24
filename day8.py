from collections import defaultdict
import helper


input_file = 'inputs/day8test'

def part_1():
  lines = helper.read_file_as_list_of_strings(input_file)
  grid = [[c for c in line] for line in lines]
  antenna_map = defaultdict(list)
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      if grid[row][col] != '.':
        antenna_map[grid[row][col]].append((row, col))

  antinode_locs = set()
  for frequency in antenna_map:
    locs = antenna_map[frequency]
    if len(locs) < 2:
      continue
    for i in range(len(locs) - 1):
      for j in range(i+1, len(locs)):
        diff_vector = (locs[j][0] - locs[i][0], locs[j][1] - locs[i][1])
        possible_antinode_locs = [(locs[j][0] + diff_vector[0], locs[j][1] + diff_vector[1]), \
                                  (locs[i][0] - diff_vector[0], locs[i][1] - diff_vector[1]), \
                                  (locs[i][0] + diff_vector[0], locs[i][1] + diff_vector[1]), \
                                  (locs[j][0] - diff_vector[0], locs[j][1] - diff_vector[1])]
        for antinode_loc in possible_antinode_locs:
          if antinode_loc not in [locs[i], locs[j]] and antinode_loc[0] >= 0 and antinode_loc[0] < len(grid) and antinode_loc[1] >= 0 and antinode_loc[1] < len(grid[0]):
            antinode_locs.add(antinode_loc)
            print(f'Antinode at {antinode_loc} for {locs[i]} and {locs[j]}')

  print(len(antinode_locs))

def part_2():
  lines = helper.read_file_as_list_of_strings(input_file)
  grid = [[c for c in line] for line in lines]
  antenna_map = defaultdict(list)
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      if grid[row][col] != '.':
        antenna_map[grid[row][col]].append((row, col))

  antinode_locs = set()
  for frequency in antenna_map:
    locs = antenna_map[frequency]
    if len(locs) < 2:
      continue
    for i in range(len(locs) - 1):
      for j in range(i+1, len(locs)):
        diff_vector = (locs[j][0] - locs[i][0], locs[j][1] - locs[i][1])
        possible_antinode_loc = locs[j]
        while possible_antinode_loc[0] >= 0 and possible_antinode_loc[0] < len(grid) and possible_antinode_loc[1] >= 0 and possible_antinode_loc[1] < len(grid[0]):
          antinode_locs.add(possible_antinode_loc)
          possible_antinode_loc = (possible_antinode_loc[0] + diff_vector[0], possible_antinode_loc[1] + diff_vector[1])
        possible_antinode_loc = locs[j]
        while possible_antinode_loc[0] >= 0 and possible_antinode_loc[0] < len(grid) and possible_antinode_loc[1] >= 0 and possible_antinode_loc[1] < len(grid[0]):
          antinode_locs.add(possible_antinode_loc)
          possible_antinode_loc = (possible_antinode_loc[0] - diff_vector[0], possible_antinode_loc[1] - diff_vector[1])

  print(len(antinode_locs))



part_1()
part_2()