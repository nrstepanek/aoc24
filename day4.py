
import helper

input_file = 'inputs/day4'

xmas = 'XMAS'

def search_xmas(char_grid, row, col, d_row, d_col, letter_i):
  if letter_i == len(xmas):
    return True
  if row < 0 or row >= len(char_grid) or col < 0 or col >= len(char_grid[0]):
    return False
  if char_grid[row][col] == xmas[letter_i]:
    return search_xmas(char_grid, row + d_row, col + d_col, d_row, d_col, letter_i + 1)
  return False

def part_1():
  lines = helper.read_file_as_list_of_strings(input_file)
  char_grid = [[c for c in line] for line in lines]
  width = len(char_grid[0])
  height = len(char_grid)
  xmas_count = 0
  for row in range(0, height):
    for col in range(0, width):
      if char_grid[row][col] == 'X':
        if search_xmas(char_grid, row, col, 1, 1, 0):
          xmas_count += 1
        if search_xmas(char_grid, row, col, 1, 0, 0):
          xmas_count += 1
        if search_xmas(char_grid, row, col, 1, -1, 0):
          xmas_count += 1
        if search_xmas(char_grid, row, col, 0, 1, 0):
          xmas_count += 1
        if search_xmas(char_grid, row, col, 0, -1, 0):
          xmas_count += 1
        if search_xmas(char_grid, row, col, -1, 1, 0):
          xmas_count += 1
        if search_xmas(char_grid, row, col, -1, 0, 0):
          xmas_count += 1
        if search_xmas(char_grid, row, col, -1, -1, 0):
          xmas_count += 1
  print(xmas_count)

def is_x_mas(char_grid, row, col):
  if row < 1 or row >= len(char_grid) - 1 or col < 1 or col >= len(char_grid[0]) - 1:
    return False
  if ((char_grid[row-1][col-1] == 'M' and char_grid[row+1][col+1] == 'S') or (char_grid[row-1][col-1] == 'S' and char_grid[row+1][col+1] == 'M')) and \
     ((char_grid[row-1][col+1] == 'M' and char_grid[row+1][col-1] == 'S') or (char_grid[row-1][col+1] == 'S' and char_grid[row+1][col-1] == 'M')):
    return True
  return False

def part_2():
  lines = helper.read_file_as_list_of_strings(input_file)
  char_grid = [[c for c in line] for line in lines]
  width = len(char_grid[0])
  height = len(char_grid)
  x_mas_count = 0
  for row in range(0, height):
    for col in range(0, width):
      if char_grid[row][col] == 'A':
        if is_x_mas(char_grid, row, col):
          x_mas_count += 1
  print(x_mas_count)

part_1()
part_2()