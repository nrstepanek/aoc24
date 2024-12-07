
import copy
import helper


input_file = 'inputs/day6'


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def pos_in_bounds(pos, grid):
  return pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(grid) and pos[1] < len(grid[0])

def part_1():
  lines = helper.read_file_as_list_of_strings(input_file)
  grid = [[c for c in line] for line in lines]

  found_guard = False
  row = 0
  col = 0
  while not found_guard:
    if grid[row][col] == '^':
      found_guard = True
    else:
      col += 1
      if col == len(grid[row]):
        col = 0
        row += 1

  guard = (row, col)
  dir_i = 0
  positions_seen = 0
  while pos_in_bounds(guard, grid):
    print(guard)
    new_guard = (guard[0] + directions[dir_i][0], guard[1] + directions[dir_i][1])
    while pos_in_bounds(new_guard, grid) and grid[new_guard[0]][new_guard[1]] == '#':
      dir_i = (dir_i + 1) % 4
      new_guard = (guard[0] + directions[dir_i][0], guard[1] + directions[dir_i][1])
    if grid[guard[0]][guard[1]] != 'X': 
      positions_seen += 1
      grid[guard[0]][guard[1]] = 'X'
    guard = new_guard

  print(positions_seen)


def make_move(grid, guard, dir_i):
  new_guard = (guard[0] + directions[dir_i][0], guard[1] + directions[dir_i][1])
  if pos_in_bounds(new_guard, grid) and grid[new_guard[0]][new_guard[1]] == '#':
    dir_i = (dir_i + 1) % 4
  else:
    guard = new_guard

  return guard, dir_i

def simulate(grid, guard, dir_i, states_seen):
  positions_seen = 0
  loop_wall_locs = set()
  while pos_in_bounds(guard, grid) and (guard, dir_i) not in states_seen:

    states_seen.add((guard, dir_i))
    guard, dir_i = make_move(grid, guard, dir_i)

    if pos_in_bounds(guard, grid) and grid[guard[0]][guard[1]] != 'X': 
      positions_seen += 1
      grid[guard[0]][guard[1]] = 'X'

  if pos_in_bounds(guard, grid):
    return positions_seen, len(loop_wall_locs), "LOOP"
  else:
    return positions_seen, len(loop_wall_locs), "END"

def part_2():
  lines = helper.read_file_as_list_of_strings(input_file)
  grid = [[c for c in line] for line in lines]

  found_guard = False
  row = 0
  col = 0
  while not found_guard:
    if grid[row][col] == '^':
      found_guard = True
    else:
      col += 1
      if col == len(grid[row]):
        col = 0
        row += 1

  guard = (row, col)
  dir_i = 0
  loop_count = 0
  for row_i in range(len(grid)):
    for col_i in range(len(grid[0])):
      if grid[row_i][col_i] == '.':
        new_grid = copy.deepcopy(grid)
        new_grid[row_i][col_i] = '#'
        simulate_result = simulate(new_grid, guard, dir_i, set())
        guard = (row, col)
        dir_i = 0
        print(simulate_result)
        if simulate_result[2] == "LOOP":
          loop_count += 1
  print(loop_count)

part_1()
part_2()
