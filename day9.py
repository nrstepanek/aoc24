
import helper


input_file = 'inputs/day9'

def disk_map_to_layout(disk_map_str):
  disk_map_nums = [int(c) for c in disk_map_str]
  on_file = True
  layout = []
  file_id = 0
  for num in disk_map_nums:
    if on_file:
      layout.extend([str(file_id)] * num)
      file_id += 1
    else:
      layout.extend(['.'] * num)
    on_file = not on_file
  return layout

def compact_layout(layout):
  free_i = 0
  while layout[free_i] != '.':
    free_i += 1
  file_i = len(layout) - 1
  while layout[file_i] == '.':
    file_i -= 1

  while free_i < file_i:
    if layout[free_i] == '.':
      layout = layout[:free_i] + [layout[file_i]] + layout[free_i+1:file_i] + ['.'] + layout[file_i+1:]
      file_i -= 1
      while layout[file_i] == '.':
        file_i -= 1
    free_i += 1
    while layout[free_i] != '.':
      free_i += 1

  return layout

def calculate_checksum(layout):
  i = 0
  checksum = 0
  while layout[i] != '.':
    checksum += int(layout[i]) * i
    i += 1

  return checksum

def part_1():
  line = helper.read_file_as_string(input_file)
  print(line)
  layout_str = disk_map_to_layout(line)
  print(layout_str)
  compacted_str = compact_layout(layout_str)
  print(compacted_str)
  checksum = calculate_checksum(compacted_str)
  print(checksum)

def disk_map_to_layout_2(disk_map_str):
  disk_map_nums = [int(c) for c in disk_map_str]
  on_file = True
  layout = []
  file_id = 0
  for num in disk_map_nums:
    if on_file:
      layout.append((str(file_id), num))
      file_id += 1
    else:
      layout.append(('.', num))
    on_file = not on_file
  return layout

def compact_layout_2(layout):
  file_i = len(layout) - 1
  while layout[file_i][0] == '.':
    file_i -= 1

  while file_i >= 0:
    #print(layout)
    size = layout[file_i][1]
    #print('Looking for free space for file {} of size {}'.format(layout[file_i][0], size))
    free_i = 0
    while free_i < file_i and (layout[free_i][0] != '.' or layout[free_i][1] < size):
      free_i += 1

    if free_i < file_i and layout[free_i][0] == '.' and layout[free_i][1] >= size:
      #print('Moving file {} to free space {}'.format(layout[file_i][0], free_i))
      leftover_space = layout[free_i][1] - size
      layout[free_i] = (layout[file_i][0], size)
      layout[file_i] = ('.', layout[file_i][1])
      if leftover_space:
        layout.insert(free_i+1, ('.', leftover_space))

    file_i -= 1
    while layout[file_i][0] == '.':
      file_i -= 1

  return layout

def create_layout(compacted):
  layout = []
  for entry in compacted:
    layout.extend([entry[0]] * entry[1])

  return layout

def calculate_checksum_2(layout_str):
  i = 0
  checksum = 0
  while i < len(layout_str):
    if layout_str[i] != '.':
      checksum += int(layout_str[i]) * i
    i += 1

  return checksum

def part_2():
  line = helper.read_file_as_string(input_file)
  print(line)
  layout = disk_map_to_layout_2(line)
  print(layout)
  compacted = compact_layout_2(layout)
  print(compacted)
  layout_str = create_layout(compacted)
  print(layout_str)
  checksum = calculate_checksum_2(layout_str)
  print(checksum)

part_2()