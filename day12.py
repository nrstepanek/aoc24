
import helper


input = 'inputs/day12'
seen_locs = set()
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def calculate_region_price(grid, row, col, region_char):
  if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
    return (0, 0, 'OUT')
  if grid[row][col] != region_char:
    return (0, 0, 'DIFFERENT')
  if (row, col) in seen_locs:
    return (0, 0, 'SEEN')
  seen_locs.add((row, col))
  area = 1
  perimiter = 0
  for dir in dirs:
    result = calculate_region_price(grid, row + dir[0], col + dir[1], region_char)
    if result[2] == 'DIFFERENT' or result[2] == 'OUT':
      perimiter += 1
    if result[2] == 'SAME':
      area += result[0]
      perimiter += result[1]

  return (area, perimiter, 'SAME')

def part_1():
  lines = helper.read_file_as_list_of_strings(input)
  grid = [[c for c in line] for line in lines]
  total_price = 0
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if (row, col) in seen_locs:
        continue
      area, perimiter, _ = calculate_region_price(grid, row, col, grid[row][col])
      print('Found region with area', area, 'and perimiter', perimiter)
      total_price += area * perimiter

  print(total_price)


def calculate_region(grid, row, col, region_char):
  if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
    return (0, [], 'OUT')
  if grid[row][col] != region_char:
    return (0, [], 'DIFFERENT')
  if (row, col) in seen_locs:
    return (0, [], 'SEEN')
  seen_locs.add((row, col))
  area = 1
  perimiter = set()
  for dir in dirs:
    result = calculate_region(grid, row + dir[0], col + dir[1], region_char)
    if result[2] == 'DIFFERENT' or result[2] == 'OUT':
      perimiter.add((row, col, dir))
    if result[2] == 'SAME':
      area += result[0]
      perimiter.update(result[1])

  return (area, perimiter, 'SAME')

def count_sides(perimiter):
  num_sides = 0
  while len(perimiter) > 0:
    row, col, dir = perimiter.pop()
    if dir[0] == 0:
      bound_0 = row - 1
      bound_1 = row + 1
      done = False
      while not done:
        done = True
        if (bound_0, col, dir) in perimiter:
          perimiter.remove((bound_0, col, dir))
          bound_0 -= 1
          done = False
        if (bound_1, col, dir) in perimiter:
          perimiter.remove((bound_1, col, dir))
          bound_1 += 1
          done = False
    else:
      bound_0 = col - 1
      bound_1 = col + 1
      done = False
      while not done:
        done = True
        if (row, bound_0, dir) in perimiter:
          perimiter.remove((row, bound_0, dir))
          bound_0 -= 1
          done = False
        if (row, bound_1, dir) in perimiter:
          perimiter.remove((row, bound_1, dir))
          bound_1 += 1
          done = False
    num_sides += 1

  return num_sides

def part_2():
  lines = helper.read_file_as_list_of_strings(input)
  grid = [[c for c in line] for line in lines]
  total_price = 0
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if (row, col) in seen_locs:
        continue
      area, perimiter, _ = calculate_region(grid, row, col, grid[row][col])
      print('Found region with area', area, 'and perimiter', perimiter)
      num_sides = count_sides(perimiter)
      print('Num sides:', num_sides)
      total_price += area * num_sides

  print(total_price)

part_2()